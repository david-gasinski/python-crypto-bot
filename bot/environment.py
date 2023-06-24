from dotenv import load_dotenv
import os

load_dotenv()

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
PREFIXES_FILE = os.getenv("PREFIXES_FILE")