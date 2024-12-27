from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Optional

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class CalendarManager:  
    SCOPES = ["https://www.googleapis.com/auth/calendar"]
    TOKEN_PATH = Path("token.json")
    CREDS_PATH = Path("client.json")
    
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

