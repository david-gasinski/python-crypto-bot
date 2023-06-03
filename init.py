from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
from commands.eth import Eth
from db import DB
#from commands.add_wallet import Wallet

load_dotenv()
TOKEN = os.getenv('TOKEN')
DB_PATH = os.getenv('DB')

if __name__ == "__main__":  
    intent = discord.Intents.default()
    intent.message_content = True #v2
    bot = commands.Bot(command_prefix='!', intents=intent)


    @bot.event
    async def on_ready():
         db = DB(DB_PATH)
         await bot.add_cog(Eth(bot))
    #bot.add_cog(Wallet(bot))
    bot.run(TOKEN)