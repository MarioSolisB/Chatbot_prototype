TOOL_LIST = [
    {
        "type": "function",
        "function": {
            "name": "send_brochure",
            "description": "Send a property brochure to the client",
            "parameters": {
                "type": "object",
                "properties": {
                    "unit_number": {"type": "string"},
                    "email": {"type": "string"}
                },
                "required": ["unit_number"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "schedule_visit",
            "description": "Schedule a property viewing appointment",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {"type": "string"},
                    "time": {"type": "string"},
                    "client_name": {"type": "string"},
                    "email": {"type": "string"}
                },
                "required": ["date", "time", "client_name"]
            }
        }
    }
]