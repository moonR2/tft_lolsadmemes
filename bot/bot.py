import os
from dotenv import load_dotenv
from discord.ext import commands
import discord

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

if not DISCORD_TOKEN:
    raise Exception("Missing DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

bot.run(DISCORD_TOKEN)
