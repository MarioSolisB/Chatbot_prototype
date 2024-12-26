import os
from dotenv import load_dotenv


load_dotenv(".env")

# --- OpenAI ---
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# --- Anthropic ---
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# --- Telegram ---
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# --- GPT model ----
GPT_MODEL = "gpt-4o-mini" #"gpt-4o"

# --- Temperature ---
TEMPERATURE = 0.1

# --- Agent Names ---
REAL_ESTATE_AGENT_NAME = "NEXUS_Agent"
USER_PROXY_NAME = "Client"

# --- Interface Settings ---
CLEAR_COMMAND = "clear"
EXIT_COMMAND = "exit"

SLEEP_TIME_BETWEEN_RETRIEVALS = 1