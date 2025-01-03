from chatbot_graph.tools.book_visit.book_visit import book_visit_tool
from chatbot_graph.tools.get_available_slots.get_available_slots import get_available_slots_tool
from chatbot_graph.tools.getcurrentweather.getcurrentweather import get_current_weather_tool



TOOLS = [
    get_available_slots_tool,
    #get_current_weather_tool,
    book_visit_tool,
]
