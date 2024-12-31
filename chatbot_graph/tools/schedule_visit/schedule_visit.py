from chatbot_graph.integrations.googlecalendar.google_calendar_manager import CalendarManager
import json

schema = {
    "name": "schedule_visit",
    "description": "Schedule a visit in google calendar.",
    "parameters": {
        "type": "object",
        "properties": {
            "date": {
                "type": "string",
                "description": "Date of the visit (YYYY-MM-DD)"
            },
            "time": {
                "type": "string",
                "description": "Hour of the visit (format: HH:MM)"
            },
            "email": {
                "type": "string",
                "description": "Email of the user (attendees)"
            }
        },
        "required": ["date", "time", "email"]  # Clearly specify required fields
    }
}

schedule_visit_tool = {
    "type": "function",
    "function": schema,
}

def schedule_visit(date, time, email):
    try:
        calendar = CalendarManager()
        
        start_time = f"{date}T{time}:00"
        end_time = f"{date}T{int(time.split(':')[0])+1}:{time.split(':')[1]}:00"
        timezone = "America/Argentina/Buenos_Aires"
        
        event = calendar.create_event(
            title=f"Visit Nexus Residences with {email}",
            start_time=start_time,
            end_time=end_time,
            timezone=timezone,
            description="Welcome to Nexus Residences! We're excited to show you our luxury apartments featuring modern amenities, stunning views, and prime location. Our team will be waiting for you at the main lobby.",
            location="Nexus Residences, Av. del Libertador 4444, Buenos Aires",
            attendees=[email],
            virtual=False
        )
        
        return json.dumps({
            "status": "success" if event else "error",
            "message": "Visit scheduled successfully" if event else "Failed to schedule visit"
        })
    except Exception as e:
        return json.dumps({
            "status": "error",
            "message": f"Failed to schedule visit: {str(e)}"
        })