# initliase bot here
import discord

class Bot(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')
