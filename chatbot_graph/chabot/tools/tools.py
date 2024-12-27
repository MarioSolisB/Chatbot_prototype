TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "send_pdf",
            "description": "Envía un archivo PDF al cliente, puede ser el brochure del condomino o la ficha de la propiedad/unidad especifica.",
            "parameters": {
                "type": "object",
                "properties": {
                    "pdf_path": {
                        "type": "string",
                        "description": "La ruta al archivo PDF del brochure que se enviará."
                    }
                },
                "required": ["pdf_path"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "agendar_visita",
            "description": "Guardar información y agendar visita de la propiedad.",
            "parameters": {
                "type": "object",
                "properties": {
                    "nombre": {
                        "type": "string",
                        "description": "Nombre del cliente"
                    },
                    "apellido": {
                        "type": "string",
                        "description": "Apellido del cliente"
                    },
                    "telefono": {
                        "type": "string",
                        "description": "Número telefónico del cliente"
                    },
                    "fecha": {
                        "type": "string",
                        "description": "Fecha de la reserva del cliente"
                    },
                    "horario_de_visita": {
                        "type": "string",
                        "description": "Horario de la visita: en forma de 24 hrs."
                    }
                },
                "required": ["nombre", "apellido", "telefono", "fecha", "horario_de_visita"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "enviar_video",
            "description": "Enviar video del condominio.",
            "parameters": {
                "type": "object",
                "properties": {
                    "video_path": {
                        "type": "string",
                        "description": "la ruta del video que se le enviará al cliente."
                    }
                },
                "required": ["video_path"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "simular_credito_hipotecario",
            "description": "Simula un crédito hipotecario basado en el monto, plazo y tasa de interés anual.",
            "parameters": {
                "type": "object",
                "properties": {
                    "monto_prestamo": {
                        "type": "number",
                        "description": "El monto total del préstamo."
                    },
                    "plazo_anos": {
                        "type": "number",
                        "description": "Plazo del préstamo en años."
                    }
                },
                "required": ["monto_prestamo", "plazo_anos"]
            }
        }
    },
#     {
#         "type": "function",
#         "function": {
#             "name": "get_photo_links",
#             "description": "Obtiene una lista de enlaces de fotos de las amenities del condominio en formato JSON.",
#             "parameters": {
#                 "type": "object",
#                  "properties": {
#                 "amenities_links": {
#                     "type": "object",
#                     "properties": {
#                         "pileta": {"type": "string"},
#                         "SUM": {"type": "string"},
#                         "Salón de Juegos": {"type": "string"},
#                         "Gimnasio": {"type": "string"}
#                     },
#                     "description": "Objeto con los nombres de las amenities como claves y sus respectivos enlaces como valores."
#                 }
#             },
#             "required": ["amenities_links"]
#         }
#     }
# }
 {
        "type": "function",
        "function": {
            "name": "check_calendar_availability",
            "description": "Verifica la disponibilidad en el calendario de Google para un rango de fechas especificado.",
            "parameters": {
                "type": "object",
                "properties": {
                    "start_date": {
                        "type": "string",
                        "description": "Fecha de inicio para verificar disponibilidad (formato: YYYY-MM-DD)."
                    },
                    "end_date": {
                        "type": "string",
                        "description": "Fecha de fin para verificar disponibilidad (formato: YYYY-MM-DD)."
                    }
                },
                "required": ["start_date", "end_date"]
            }
        }
    },
    {
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
]
