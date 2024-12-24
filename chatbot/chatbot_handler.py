from openai import OpenAI

class ChatBot:
    def __init__(self, api_key, model, prompt, some_tools=None):
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.prompt = prompt
        self.some_tools = some_tools

    def get_response(self, messages):
        try:
            # Prepare messages with system prompt
            prompt = [
                {
                    "role": "system",
                    "content": self.prompt
                }
            ]
            prompt.extend(messages)

            # Prepare API call parameters
            params = {
                "model": self.model,
                "messages": prompt,
                "temperature": 0.1
            }

            # Only add tools if they are provided
            if self.some_tools:
                params["tools"] = self.some_tools

            # Get response from OpenAI
            response = self.client.chat.completions.create(**params)

            # Get the message from the response
            message = response.choices[0].message

            # Create assistant message
            assistant_message = {
                "role": "assistant",
                "content": message.content if message.content else "",
            }

            # Add tool_calls only if they exist
            if hasattr(message, 'tool_calls') and message.tool_calls:
                assistant_message["tool_calls"] = message.tool_calls[0]
            else:
                assistant_message["tool_calls"] = None

            return assistant_message

        except Exception as e:
            print(f"Error in ChatBot: {e}")
            return {
                "role": "assistant",
                "content": "I encountered an error processing your message.",
                "tool_calls": None
            }