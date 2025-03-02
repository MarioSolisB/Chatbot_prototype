import anthropic
import json
from datetime import datetime
import pytz

from chatbot_graph_claude.tools.tools import TOOLS
from chatbot_graph.tools.getcurrentweather.getcurrentweather import get_current_weather


class ChatBot_Claude:
    def __init__(self, api_key, gpt_model, base_system_prompt):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.gpt_model = gpt_model
        self.base_system_prompt = base_system_prompt
        self.messages = [ ]

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
            "system": self._get_system_prompt(),
            "model": self.gpt_model,
            "messages": self.messages,
            "temperature": 0.1,
            "max_tokens":500,
            "tools": TOOLS,
            #"tool_choice": "auto",
            }
        
        response = self.client.messages.create(**parameters)
        print(f"""
***************************** LOGS RESPONSE *******************************************
>>>>> Response: {response}
***************************************************************************************
""")
        
        tool_calls_action = response.stop_reason
        assistant_message = response.content[0].text

        if tool_calls_action == "tool_use":
            tool_calls_action = True
            tool_calls = response.content[1]
        else:
            tool_calls_action = False
            tool_calls = None
   
        
        return self.messages, assistant_message, tool_calls_action, tool_calls
         
    def process_tool_calls(self, messages, assistant_message, tool_calls):
        function_handlers = {
            #"book_visit": book_visit,
            #"get_available_slots": get_available_slots,
            "get_current_weather": get_current_weather, # change to a my list of tools
            #"get_stock_price": get_stock_price,        
            #"analyze_sentiment": analyze_sentiment,
            # Add more functions here as needed
            }
        
        content = [{
                "type": "text",
                "text": assistant_message,
            }
        ]
        print(f"""
***************************************************************************************
>>>>> Tool calls: {tool_calls}
***************************************************************************************
""")
        # For list/tuple problem of tool_calls
        if isinstance(tool_calls, (list, tuple)):  
            tool_calls_dict = [
                {
                    "type": tool_call.type,
                    "id": tool_call.id,
                    "name": tool_call.name,
                    "input": tool_call.input,
                }
                for tool_call in tool_calls
            ]
        else:  
            tool_calls_dict = [{
                "type": tool_calls.type,
                "id": tool_calls.id,
                "name": tool_calls.name,
                "input": tool_calls.input,
            }]

        assistant_message_dict = {
            "role": "assistant",
            "content": tool_calls_dict
        }

        messages.append(assistant_message_dict)
        print(f"""
***************************************************************************************
>>>>> Messages: {json.dumps(messages, indent=4)}
***************************************************************************************
""")
        if isinstance(tool_calls, (list, tuple)):

            for tool_call in tool_calls:
                function_name = tool_call.name
                # ---- Log control of Calling function ---
                print(f"""
************************* LOGS CALLING FUNCTION ***************************************
>>>>> Calling function: {function_name}
***************************************************************************************
""")
                function_args = json.loads(tool_call.input)
                

                # Get the appropriate function handler
                handler = function_handlers.get(function_name)

                function_response = handler(**function_args)
                # --- Log control of function response ----
                print(f"""
************************* LOGS FUNCTION RESPONSE **************************************
>>>>> Function response: {json.dumps(function_response, indent=4)}
***************************************************************************************
""")
                tool_response = {
                "role": "user",
                "content": [
                    {
                        "type": "tool_result",
                        "tool_use_id": tool_calls.id,
                        "content": function_response,
                        }
                    ] 
                }
                
                messages.append(tool_response)
                print(f"""
***************************************************************************************
>>>>> Messages: {json.dumps(messages, indent=4)}
***************************************************************************************
""")
                
        else:
            function_name = tool_calls.name
            print(f"""
************************* LOGS CALLING FUNCTION ***************************************
>>>>> Calling function: {function_name}
***************************************************************************************
""")
            function_args = tool_calls.input
            

            # Get the appropriate function handler
            handler = function_handlers.get(function_name)

            function_response = handler(**function_args)
            # --- Log control of function response ----
            print(f"""
************************* LOGS FUNCTION RESPONSE **************************************
>>>>> Function response: {json.dumps(function_response, indent=4)}
***************************************************************************************
""")
            tool_response = {
                "role": "user",
                "content": [
                    {
                        "type": "tool_result",
                        "tool_use_id": tool_calls.id,
                        "content": function_response,
                        }
                    ] 
            }
            
            messages.append(tool_response)
            print(f"""
***************************************************************************************
>>>>> Messages: {json.dumps(messages, indent=4)}
***************************************************************************************
""")
        

        parameters = {
            "system": self._get_system_prompt(),
            "model": self.gpt_model,
            "messages": self.messages,
            "temperature": 0.1,
            "max_tokens":500,
            "tools": TOOLS,
            #"tool_choice": "auto",
            }
        
        function_enriched_response = self.client.messages.create(**parameters)

        assistant_message_enriched = function_enriched_response.content[0].text
        tool_calls_action_enriched = function_enriched_response.stop_reason

        if tool_calls_action_enriched == "tool_use":
            tool_calls_action_enriched = True
            tool_calls_enriched = function_enriched_response.content[1]
        else:
            tool_calls_action_enriched = False
            tool_calls_enriched = None
   
        
        return messages, assistant_message_enriched, tool_calls_action_enriched, tool_calls_enriched #function_enriched_response #

    def get_response_final(self, user_input):
        messages, assistant_message, tool_calls_action, tool_calls  = self.get_response(user_input)
            
        if tool_calls_action == False: 
            assistant_message = {
            "role": "assistant",
            "content":assistant_message,
            }
            messages.append(assistant_message)
            # Control log of messages
#             print(f"""
# ************************* LOGS MESSAGES ***********************************************
# >>>> Adding to messages: {json.dumps(messages, indent=2)}
# ***************************************************************************************
# """)

            return messages, assistant_message, tool_calls_action, tool_calls
        else:
            messages, assistant_message_enriched, tool_calls_action_enriched, tool_calls_enriched = self.process_tool_calls(messages, assistant_message, tool_calls)
            assistant_message = {
            "role": "assistant",
            "content":assistant_message_enriched,
            }
            messages.append(assistant_message)
            # Control log of messages
#             print(f"""
# ************************* LOGS MESSAGES ***********************************************
# >>>> Adding to messages: {json.dumps(messages, indent=2)}
# ***************************************************************************************
# """)

            return messages, assistant_message, tool_calls_action_enriched, tool_calls_enriched