from openai import OpenAI
import json

class ChatBot:
    def __init__(self, api_key, model, prompt, some_tools):
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.prompt = prompt
        self.some_tools = some_tools

    def get_response(self, messages):
        # Prepare messages with system prompt
        prompt = [
            {
                "role": "system",
                "content": self.prompt
            }
        ]
        prompt.extend(messages)

        # Get response from OpenAI
        response = self.client.chat.completions.create(
            model=self.model,
            messages=prompt,
            temperature=0.1,
            tools=self.some_tools
        )

        # Initialize tool_calls
        tool_calls = None

        # Check for tool calls in response
        if response.choices[0].message.tool_calls:
            tool_calls = response.choices[0].message.tool_calls[0]

        # Create assistant message
        assistant_message = {
            "role": "assistant",
            "content": response.choices[0].message.content,
            "tool_calls": tool_calls
        }
            
        return assistant_message