from aiogram import types

class TelegramMessageHandler:
    def __init__(self, chatbot):
        self.chatbot = chatbot
        self.chat_history = {}

    async def handle_message(self, message: types.Message):
        user_id = message.from_user.id
        user_message = message.text
        
        # Initialize chat history for new users
        if user_id not in self.chat_history:
            self.chat_history[user_id] = []
            
        # Add user message to history
        self.chat_history[user_id].append({
            "role": "user",
            "content": user_message
        })

        try:
            # Get chatbot response
            response = self.chatbot.get_response(self.chat_history[user_id])
            
            # Add bot response to history
            if response:
                self.chat_history[user_id].append(response)
                
                # Handle the response content
                if response.get("content"):
                    await message.reply(response["content"], parse_mode="Markdown")
                
                # Handle tool calls if present
                if response.get("tool_calls"):
                    tool_name = response["tool_calls"].function.name
                    await message.reply(f"Using tool: {tool_name}")
                    # Add tool handling logic here if needed

        except Exception as e:
            print(f"Error processing message: {e}")
            await message.reply("Sorry, I encountered an error processing your message.")