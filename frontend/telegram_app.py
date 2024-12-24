from aiogram import Bot, Dispatcher, executor, types
from telegram_handler import TelegramMessageHandler
from config import TELEGRAM_TOKEN


# Initialize bot
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

# Initialize chatbot and handler
chatbot = {
    "get_response": lambda msg, 
    history: {
        "role": "assistant",
        "content": "Bot response here"
        }
}

message_handler = TelegramMessageHandler(chatbot)

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.reply("Chat started!")

@dp.message_handler()
async def handle_message(message: types.Message):
    await message_handler.handle_message(message)

if __name__ == "__main__":
    executor.start_polling(dp)