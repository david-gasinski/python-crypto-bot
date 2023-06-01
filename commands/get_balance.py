import discord
from bot import Bot

class Balance(commands.Cog):
    def __init__(self,bot : Bot):
        self.bot = bot

    @commands.command()
    async def get_balance(self, wallet: str, coin: str):
        """ gets balance of supplied wallet"""
        
