def send_brochure(unit_number: str, email: str = None) -> str:
    return f"[IN CRM: Sending brochure for unit {unit_number} to {email if email else 'client'}]"

def schedule_visit(date: str, time: str, client_name: str, email: str = None) -> str:
    return f"[IN CRM: Scheduling visit for {client_name} on {date} at {time}]"