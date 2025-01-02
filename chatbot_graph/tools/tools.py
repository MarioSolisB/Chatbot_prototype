from chatbot_graph.tools.schedule_visit.schedule_visit import schedule_visit_tool
from chatbot_graph.tools.get_available_slots.get_available_slots import get_available_slots_tool
from chatbot_graph.tools.getcurrentweather.getcurrentweather import get_current_weather_tool



TOOLS = [
    get_available_slots_tool,
    get_current_weather_tool,
    #schedule_visit_tool,
]
