# NEXUS Residences Chatbot

A sophisticated Telegram-based real estate chatbot designed to assist potential residents with property information, scheduling visits, and managing appointments for NEXUS Residences. The chatbot uses a structured conversation flow graph to provide a coherent and effective interaction with users.

## Key Features

- Graph-based conversation flow management
- Automated property information delivery
- Smart appointment scheduling through Google Calendar
- Property visit management
- Customized responses based on user preferences
- Real-time availability checking
- Timezone handling
- PDF brochure sharing capabilities
- Financing information delivery

## Conversation Flow Graph
The chatbot implements a sophisticated directed graph structure where:

- Nodes represent different conversation states (greeting, property showing, visit scheduling, etc.)
- Edges define the possible transitions between states
- Each transition has specific conditions and response expectations
- The conversation always starts at the "identify_first_message" node

Key conversation states include:

- Initial greeting and preference gathering
- Property information showcase
- Doubt resolution
- Visit scheduling
- Financing information
- Advisor referral


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
│   ├── tools/
│   │    ├── book_visit/
│   │    │   └── book_visit.py
│   │    ├── get_available_slots/
│   │    |   └── get_available_slots
│   │    └── tools.py
│   ├── chatbot_handler.py
│   ├── flow_graph.py
│   └── prompt.py
├── interface/
│   └── telegram_app.py
```

## Requirements

- Python 3.11.9
- Google Calendar API credentials
- Telegram Bot Token
- Google Sheets integration (for property data)

## Setup

1. Clone the repository
2. Install the required dependencies
3. Configure the Google Calendar credentials:
   - Place your `client.json` in the `googlecalendar` directory
   - Run the authentication flow to generate `token.json`
4. Set up your Telegram bot token
5. Configure the timezone in `book_visit.py` if needed

## Usage

The chatbot handles:

- Property inquiries and information requests
- Visit scheduling with required fields:

   - Date   
   - Time (Format: HH:MM)
   - Email (for attendees)

- Financing information requests
- Property documentation sharing

## Development

The project uses a modular structure:
- `flow_graph.py`: Defines the conversation flow structure
- `chatbot_handler.py`: Main bot logic
- `book_visit.py`: Appointment scheduling functionality
- `google_calendar_manager.py`: Google Calendar API interactions
- `telegram_app.py`: Telegram bot implementation
