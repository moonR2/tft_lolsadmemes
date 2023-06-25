import os
import asyncio
from dotenv import load_dotenv
from discord.ext import commands
import discord

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

if not DISCORD_TOKEN:
    raise Exception("Missing DISCORD_TOKEN")

"""
This function will create the bot and return it
"""
async def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='.', intents=intents)

    @bot.event
    async def on_ready():
        print(f'{bot.user} has connected to Discord!')


    return bot

"""
This function will load all the COGS from the commands folder
"""
async def load_extensions(bot):
    for filename in os.listdir('./bot/commands'):
            if filename.endswith('.py'):
                await bot.load_extension(f'commands.{filename[:-3]}')

"""
This is the main function that will be executed, needs to be async since load_extensions
needs to be awaited.
"""
async def main():
    bot = await run_discord_bot()
    async with bot:
        await load_extensions(bot)
        await bot.start(DISCORD_TOKEN)

"""
This is the entrypoint of the program, it will run the main function and handle
"""
asyncio.run(main())

