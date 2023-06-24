import discord
import discord.ext.commands
import json
from environment import DISCORD_BOT_TOKEN, PREFIXES_FILE

DEFAULT_PREFIX = "!"
DEFAULT_LANGUAGE="en"

# get custom prefixes
def retrieve_prefix(client, message):
    with open(PREFIXES_FILE, 'r') as f:
        prefixes = json.load(f)
        f.close()
        return prefixes[str(message.guild.id)]
    
# create client
intents = discord.Intents.default()
intents.message_content = True

bot = discord.ext.commands.Bot(command_prefix=(retrieve_prefix), intents=intents)


# set default prefix when joining guild 
@bot.event
async def on_guild_join(guild):
    with open(PREFIXES_FILE, 'r') as f:
        prefixes = json.load(f)
        f.close()
    prefixes[str(guild.id)] = DEFAULT_PREFIX
    with open(PREFIXES_FILE, 'w') as f:
        json.dump(prefixes, f, indent=4)
        f.close()
    await guild.system_channel.send("word")
        
# remove prefix when leaving guild
@bot.event
async def on_guild_remove(guild):
    with open(PREFIXES_FILE, 'r') as f:
        prefixes = json.load(f)
        f.close()
    prefixes.pop(str(guild.id))
    with open(PREFIXES_FILE, 'w') as f:
        json.dump(prefixes, f, indent=4)
        f.close()
        
    
# change prefixes
@bot.command(pass_context=True)
@discord.ext.commands.has_permissions(administrator=True)
async def changePrefix(ctx, prefix):
    with open(PREFIXES_FILE, 'r') as f:
        prefixes = json.load(f)
        f.close()
    prev_prefix = prefixes[str(ctx.guild.id)]
    prefixes[str(ctx.guild.id)] = prefix
    with open(PREFIXES_FILE, 'w') as f:
        json.dump(prefixes, f, indent=4)
        f.close()
    
    await ctx.send(f"Prefix changed to {prefix} from {prev_prefix}")



# run bot
bot.run(DISCORD_BOT_TOKEN)

        
        