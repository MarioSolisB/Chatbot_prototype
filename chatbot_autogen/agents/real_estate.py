"""Real estate agent implementation."""

import autogen
from chatbot_autogen.config.prompts import SYSTEM_PROMPT
from chatbot_autogen.config.settings import REAL_ESTATE_AGENT_NAME
from chatbot_autogen.tools.definitions import TOOL_LIST
from chatbot_autogen.tools.implementations import send_brochure, schedule_visit
from chatbot_autogen.agents.llm_config import create_llm_config

def create_real_estate_agent():
    llm_config = create_llm_config(None) #TOOL_LIST)
    
    return autogen.AssistantAgent(
        name=REAL_ESTATE_AGENT_NAME,
        system_message=SYSTEM_PROMPT,
        llm_config=llm_config,
        function_map={
            "send_brochure": send_brochure,
            "schedule_visit": schedule_visit
        }
    )