# Chatbot Prototype

A Telegram real estate chatbot that manages calendar bookings and appointments using Google Calendar integration.

## Features

- Calendar event booking through Telegram
- Integration with Google Calendar
- Available time slots checking
- Timezone handling (Default: America/Argentina/Buenos_Aires)

## Project Structure

```
chatbot_prototype/
├── chatbot_graph/
│   ├── data/
│   ├── integrations/
│   │   ├── googlecalendar/
│   │   │   ├── client.json
│   │   │   ├── google_calendar_manager.py
│   │   │   ├── token.json
│   │   │   └── pruebas.ipynb
│   │   └── googlesheet/
│   └── tools/
│   |    ├── book_visit/
│   |    │   ├── book_visit.py
│   |    ├── get_available_slots/
|   |    |   |── get_available_slots
│   |    ├── tools.py
│   |── chatbot_handler.py
│   ├── flow_graph.py
│   |── prompt.py
├── interface/
|   |── telegram_app.py
```

## Requirements

- Python 3.11.9
- Google Calendar API credentials
- Telegram Bot Token

## Setup

1. Clone the repository
2. Install the required dependencies
3. Configure the Google Calendar credentials:
   - Place your `client.json` in the `googlecalendar` directory
   - Run the authentication flow to generate `token.json`
4. Set up your Telegram bot token
5. Configure the timezone in `book_visit.py` if needed

## Usage

The bot handles appointment bookings with the following required fields:
- Date
- Time (Format: HH:MM)
- Email (for attendees)

## Development

The project uses a modular structure:
- `chatbot_handler.py`: Main bot logic
- `book_visit.py`: Appointment scheduling functionality
- `google_calendar_manager.py`: Google Calendar API interactions
- `telegram_app.py`: Telegram bot implementation
