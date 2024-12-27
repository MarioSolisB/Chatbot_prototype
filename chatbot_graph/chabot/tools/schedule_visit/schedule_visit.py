schedule_visit_tool = {
    "type": "function",
    "function": {
        "name": "schedule_calendar_visit",
        "description": "Agenda una visita en el calendario de Google.",
        "parameters": {
            "type": "object",
            "properties": {
                "summary": {
                    "type": "string",
                    "description": "Resumen o título del evento para la visita."
                },
                "start_time": {
                    "type": "string",
                    "description": "Hora de inicio para la visita (formato: YYYY-MM-DDTHH:MM:SS)."
                },
                "end_time": {
                    "type": "string",
                    "description": "Hora de fin para la visita (formato: YYYY-MM-DDTHH:MM:SS)."
                },
                "timezone": {
                    "type": "string",
                    "description": "Zona horaria para el evento (por defecto: 'America/Argentina/Buenos_Aires')."
                }
            },
            "required": ["summary", "start_time", "end_time"]
        }
    }
}