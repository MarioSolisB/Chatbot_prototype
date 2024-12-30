from chatbot_graph.integrations.googlecalendar.google_calendar_manager import CalendarManager

schema = {
    "name": "schedule_visit",
    "description": "Agenda una visita en el calendario de Google.",
    "parameters": {
        "type": "object",
        "properties": {
            "date": {
                "type": "string", 
                "description": "Día de la visita (YYYY-MM-DD)"
            },
            "time": {
                "type": "string",
                "description": "Hour of the visit (format: HH:MM)."
            },
            "email":{
                "type": "string",
                "description": "Correo del asistente (attendees)"
            },
        },
        "required": ["date", "time", "email"]
    }
}

schedule_visit_tool = {
    "type": "function",
    "function": schema,
}

def schedule_visit(date, time, email):
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
    
    return {
        "status": "success" if event else "error",
        "message": "Visit scheduled successfully" if event else "Failed to schedule visit"
    }


