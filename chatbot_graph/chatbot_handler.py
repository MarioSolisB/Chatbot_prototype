from openai import OpenAI
import json
from datetime import datetime
import pytz

from chatbot_graph.tools.tools import TOOLS
from chatbot_graph.tools.schedule_visit.schedule_visit import schedule_visit
from chatbot_graph.tools.get_available_slots.get_available_slots import get_available_slots
from chatbot_graph.tools.getcurrentweather.getcurrentweather import get_current_weather

class ChatBot:
    def __init__(self, api_key, gpt_model, base_system_prompt):
        self.client = OpenAI(api_key=api_key)
        self.gpt_model = gpt_model
        self.base_system_prompt = base_system_prompt
        self.messages = [
            {
                "role": "system",
                "content": self._get_system_prompt()
            }
        ]

    def _get_system_prompt(self):
        buenos_aires_tz = pytz.timezone('America/Argentina/Buenos_Aires')
        current_time = datetime.now(buenos_aires_tz)
        formatted_datetime = current_time.strftime('%B %d, %Y, %I:%M:%S %p %Z')
        
        return f"""
        {self.base_system_prompt}
        
        Current timestamp: {formatted_datetime} (Buenos Aires Time)
        """

    def get_response(self, user_input): 
        

        user_messages = {
            "role": "user",
            "content": user_input
        }

        self.messages.append(user_messages)

        parameters = {
            "model": self.gpt_model,
            "messages": self.messages,
            "temperature": 0.1,
            "tools": TOOLS,
            "tool_choice": "auto",
            } 

        response = self.client.chat.completions.create(**parameters)     

        assistant_message = response.choices[0].message.content
        tool_calls_action = response.choices[0].finish_reason
        tool_calls = response.choices[0].message.tool_calls

        
        if tool_calls_action == "stop":
            tool_calls_action = False
        else:
            tool_calls_action = True
        
        return self.messages, assistant_message, tool_calls_action, tool_calls

    def process_tool_calls(self, messages, assistant_message, tool_calls):
        function_handlers = {
            "schedule_visit": schedule_visit,
            "get_available_slots": get_available_slots,
            #"get_current_weather": get_current_weather, # change to a my list of tools
            #"get_stock_price": get_stock_price,        
            #"analyze_sentiment": analyze_sentiment,
            # Add more functions here as needed
            }

        tool_calls_dict = [
            {
                "id": tool_call.id,
                "type": tool_call.type,
                "function": {
                    "name": tool_call.function.name,
                    "arguments": tool_call.function.arguments
                }
            }
            for tool_call in tool_calls
        ]

        assistant_message = {
            "role": "assistant",
            "content": assistant_message, # None or null
            "tool_calls": tool_calls_dict
        }

        messages.append(assistant_message)

        for tool_call in tool_calls:
            function_name = tool_call.function.name
            # ---- Log control of Calling function ---
            print(f"""
************************* LOGS CALLING FUNCTION ***************************************
>>>>> Calling function: {function_name}
***************************************************************************************
""")
            
            function_args = json.loads(tool_call.function.arguments)
            

            # Get the appropriate function handler
            handler = function_handlers.get(function_name)

            function_response = handler(**function_args)
            # --- Log control of function response ----
            print(f"Function response: {function_response}")
            
            tool_response = {
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": function_name,
                "content": function_response,
            }
            
            messages.append(tool_response)
#             print(f"""
# ************************* LOGS MESSAGES ***********************************************
# >>>> Adding to messages: {json.dumps(messages, indent=2)}
# ***************************************************************************************
# """)

        function_enriched_response = self.client.chat.completions.create(model=self.gpt_model, messages=messages)

        assistant_message_enriched = function_enriched_response.choices[0].message.content
        tool_calls_action_enriched = function_enriched_response.choices[0].finish_reason
        tool_calls_enriched = function_enriched_response.choices[0].message.tool_calls

        if tool_calls_action_enriched == "stop":
            tool_calls_action_enriched = False
        else:
            tool_calls_action_enriched = True
        
        return messages, assistant_message_enriched, tool_calls_action_enriched, tool_calls_enriched
    

    def get_response_final(self, user_input):
        messages, assistant_message, tool_calls_action, tool_calls  = self.get_response(user_input)
            
        if tool_calls_action == False: 
            assistant_message = {
            "role": "assistant",
            "content":assistant_message,
            }
            messages.append(assistant_message)

            return messages, assistant_message, tool_calls_action, tool_calls
        else:
            messages, assistant_message_enriched, tool_calls_action_enriched, tool_calls_enriched = self.process_tool_calls(messages, assistant_message, tool_calls)
            assistant_message = {
            "role": "assistant",
            "content":assistant_message_enriched,
            }
            messages.append(assistant_message)

            return messages, assistant_message, tool_calls_action_enriched, tool_calls_enriched