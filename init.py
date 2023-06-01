from dotenv import load_dotenv
from bot import Bot
import os
import discord

load_dotenv()
TOKEN = os.getenv('TOKEN')

if __name__ == "__main__":
    intents = discord.Intents.default()
    client = Bot(intents=intents)
    client.run(TOKEN)