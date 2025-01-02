from aiogram import Bot, Dispatcher, executor, types
from config import TELEGRAM_TOKEN, OPENAI_API_KEY, gpt_model


import sys
import os
import json

# Add parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from chatbot_graph.chatbot_handler import ChatBot
from chatbot_graph.prompt import system_prompt


# --- Initialize bot ---
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

#system_prompt = "You are a helpful assistant that can access external functions. The responses from these function calls will be appended to this dialogue. Please provide responses based on the information from these function calls."

chatbot = ChatBot(OPENAI_API_KEY,gpt_model,system_prompt)


# # Function to load chat history
def load_chat_history():
    try:
        with open('backend/data_chat_history/chat_history.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Function to save chat history
def save_chat_history(chat_history):
    with open('backend/data_chat_history/chat_history.json', 'w', encoding='utf-8') as f:
        json.dump(chat_history, f, ensure_ascii=False, indent=2)


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.reply("--- Starting bot ---")

chat_history = {}

@dp.message_handler()
async def handle_messages(message:types.Message):
    user_id = message.from_user.id
    user_message = message.text

    # Initialize chat history for new users
    if user_id not in chat_history:
        chat_history[user_id] = []
        
    # Add user message to history
    chat_history[user_id].append({
        "role": "user",
        "content": user_message
    })
    
    messages, assistant_message, tool_calls_action, tool_calls =  chatbot.get_response_final(user_message) # None, "I printed your chat_history!", False, None 

    assistant_response = {
        "role": "assistant",
        "content": assistant_message["content"],
        "tool_calls_action":tool_calls_action,
        "tool_calls": tool_calls,
    }

    chat_history[user_id].append(assistant_response)

    save_chat_history(chat_history)

    # --- Control log of chat history ---    
#     print(f"""
# ************************* LOGS TELEGRAM ***************************************
# {json.dumps(chat_history, indent=2)}
# *******************************************************************************
# """)
    await message.reply(assistant_message["content"], parse_mode="Markdown")

if __name__ == "__main__":
    print("Bot started...")
    executor.start_polling(dp)