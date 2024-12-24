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

        # Get chatbot response
        response = self.chatbot.get_response(self.chat_history[user_id])
        
        # Add response to history
        self.chat_history[user_id].append(response)

        # Handle tool calls if present
        if response["tool_calls"]:
            await message.reply(f"Using tool: {response['tool_calls'].function.name}")
            # Handle tool response here if needed
        
        # Send the text response
        if response["content"]:
            await message.reply(response["content"])