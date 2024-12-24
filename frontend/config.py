import os
from dotenv import load_dotenv


load_dotenv(".env")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# --- GPT model ----
gpt_model = "gpt-4o-mini" #"gpt-4o"

SLEEP_TIME_BETWEEN_RETRIEVALS = 1