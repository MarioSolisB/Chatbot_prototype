from aiogram import Bot, Dispatcher, executor, types
from telegram_handler import TelegramMessageHandler
from config import TELEGRAM_TOKEN, OPENAI_API_KEY, gpt_model


import sys
import os

# Add parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from chatbot_graph.chatbot_handler import ChatBot
from chatbot_graph.prompt import system_prompt
from chatbot_graph.tools.tools import TOOLS


# --- Initialize bot ---
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

# --- Initialize ChatBot with configurations ---
chatbot = ChatBot(
    api_key=OPENAI_API_KEY,
    model=gpt_model,
    system_prompt=system_prompt,
)

# --- Initialize message handler ---
message_handler = TelegramMessageHandler(chatbot)

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.reply("--- Starting bot ---")

@dp.message_handler()
async def handle_message(message: types.Message):
    await message_handler.handle_message(message)

if __name__ == "__main__":
    print("Bot started...")
    executor.start_polling(dp)