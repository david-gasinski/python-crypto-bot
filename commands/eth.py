from discord.ext import commands
from db import db

class Eth(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # SET WALLET
    @commands.command(name="set")
    async def bind_wallet_to_user(self, ctx, wallet: str):
        member = ctx.author
        if (member == self.bot.user):
            return
        db.add_record(member.get_id, wallet)        
        await ctx.send(f'User {member.get_id} bound to wallet {wallet}')

    # UPDATE WALLET
    @commands.command(name="update")
    async def update_wallet(self, ctx, wallet: str):
        member = ctx.author
        if (member == self.bot.user):
            return
        
    # REMOVE WALLET
    @commands.command(name="remove")
    async def remove_wallet_from_user(self, ctx, wallet: str):
        member = ctx.author
        if (member == self.bot.user):
            return
        db.remove_record(member.get_id)
        
    @commands.command(name="get")
    async def get_eth_data(self, ctx, subcommand: str, val: str):
        pass


