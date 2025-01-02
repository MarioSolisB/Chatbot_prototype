from chatbot_graph.integrations.googlecalendar.google_calendar_manager import CalendarManager
import json

schema = {
    "name": "get_available_slots",
    "description": "Retrieve 3 available one-hour slots from Google Calendar for appointment scheduling",
    "parameters": {
        "type": "object",
        "properties": {
            "days_ahead": {
                "type": "integer",
                "description": "Number of days to look ahead (default: 3)"
            },
            "duration": {
                "type": "integer",
                "description": "Duration of the slot in minutes (default: 60)"
            }
        }
    }
}

get_available_slots_tool = {
    "type": "function",
    "function": schema,
}

def get_available_slots(days_ahead: int = 3, duration: int = 60) -> str:
    """Get available calendar slots for appointments"""
    calendar_manager = CalendarManager()
    available_slots = calendar_manager.get_available_slots(days=days_ahead, slot_duration=duration)
    return json.dumps({"available_slots": available_slots})