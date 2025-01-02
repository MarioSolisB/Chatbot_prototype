from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Optional
from zoneinfo import ZoneInfo

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class CalendarManager:  
    SCOPES = ["https://www.googleapis.com/auth/calendar"]
    TOKEN_PATH = Path("chatbot_graph/integrations/googlecalendar/token.json")
    CREDS_PATH = Path("chatbot_graph/integrations/googlecalendar/client.json")
    
    def __init__(self) -> None:
        self.service = self._get_service()

    def _get_service(self):
        creds = None
        
        if self.TOKEN_PATH.exists():
            creds = Credentials.from_authorized_user_file(str(self.TOKEN_PATH), self.SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(str(self.CREDS_PATH), self.SCOPES)
                creds = flow.run_local_server(port=0)
            
            self.TOKEN_PATH.write_text(creds.to_json())

        return build("calendar", "v3", credentials=creds)

    def get_available_slots(self, days: int = 3, slot_duration: int = 60) -> List[Dict]:
        try:
            # Get Buenos Aires timezone
            timezone = ZoneInfo("America/Argentina/Buenos_Aires")
            now = datetime.now(timezone)
            
            # Find start of next working day
            start_date = now.replace(hour=10, minute=0, second=0, microsecond=0)
            if now.hour >= 17:  # If current time is past 5 PM, start from next day
                start_date += timedelta(days=1)
            
            available_slots = []
            days_checked = 0
            current_date = start_date
            
            while days_checked < days:
                # Skip Sunday
                if current_date.weekday() == 6:  # Sunday
                    current_date += timedelta(days=1)
                    continue
                
                # Get busy periods for the current day
                day_end = current_date.replace(hour=17, minute=0)
                
                events = self.service.events().list(
                    calendarId='primary',
                    timeMin=current_date.isoformat(),
                    timeMax=day_end.isoformat(),
                    singleEvents=True,
                    orderBy='startTime'
                ).execute().get('items', [])
                
                # Convert events to busy periods
                busy_periods = []
                for event in events:
                    start = datetime.fromisoformat(event['start'].get('dateTime', event['start'].get('date')))
                    end = datetime.fromisoformat(event['end'].get('dateTime', event['end'].get('date')))
                    busy_periods.append((start, end))
                
                # Find available slots
                current_slot = current_date
                while current_slot + timedelta(minutes=slot_duration) <= day_end:
                    slot_end = current_slot + timedelta(minutes=slot_duration)
                    is_available = True
                    
                    # Check if slot overlaps with any busy period
                    for busy_start, busy_end in busy_periods:
                        if not (slot_end <= busy_start or current_slot >= busy_end):
                            is_available = False
                            break
                    
                    if is_available and len(available_slots) < 3:
                        available_slots.append({
                            "start": current_slot.isoformat(),
                            "end": slot_end.isoformat(),
                            "timezone": "America/Argentina/Buenos_Aires"
                        })
                        
                        if len(available_slots) == 3:
                            return available_slots
                    
                    current_slot += timedelta(minutes=slot_duration)
                
                current_date = (current_date + timedelta(days=1)).replace(hour=10, minute=0)
                days_checked += 1
            
            return available_slots
            
        except Exception as e:
            print(f"Error getting available slots: {e}")
            return []                                           

    def get_upcoming_events(self, days: int = 5, max_results: int = 10) -> List[Dict]:
        try:
            now = datetime.utcnow()
            time_max = (now + timedelta(days=days)).replace(hour=23, minute=59)
            
            events = self.service.events().list(
                calendarId='primary',
                timeMin=now.isoformat() + "Z",
                timeMax=time_max.isoformat() + "Z",
                maxResults=max_results,
                singleEvents=True,
                orderBy='startTime'
            ).execute().get('items', [])
            
            return events
            
        except HttpError as e:
            print(f"Error fetching events: {e}")
            return []

    def create_event(
        self, 
        title: str,
        start_time: str,
        end_time: str,
        timezone: str,
        description: Optional[str] = None,
        location: Optional[str] = None,
        attendees: Optional[List[str]] = None,
        virtual: bool = False
    ) -> Optional[Dict]:
        try:
            event = {
                "summary": title,
                "start": {"dateTime": start_time, "timeZone": timezone},
                "end": {"dateTime": end_time, "timeZone": timezone},
            }

            if description:
                event["description"] = description
            if location:
                event["location"] = location
            if attendees:
                event["attendees"] = [{"email": email} for email in attendees]

            response = self.service.events().insert(
                calendarId='primary',
                body=event,
                conferenceDataVersion=1 if virtual else 0
            ).execute()
            
            return response
            
        except HttpError as e:
            print(f"Error creating event: {e}")
            return None

