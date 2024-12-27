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

def schedule_visit(date, time, email):

    return 


schedule_visit_tool = {
    "type": "function",
    "function": schema,
}