import os
from dotenv import load_dotenv


load_dotenv(".env")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")


SLEEP_TIME_BETWEEN_RETRIEVALS = 1