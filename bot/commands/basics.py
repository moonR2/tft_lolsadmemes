# Archivo commands/hello.py
from discord.ext import commands

class Basics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send('¡Hola! 👋 soy lolsadmemes he vuelto a la vida. Larga vida a Moonify mi resucitor!')

    @commands.command()
    async def jaime(self, ctx):
        await ctx.send('Jaime alias (Jastk45) es un jugador main Diana, que se dedica a trolear partidas en MID. También de vez en cuando se dedica a jugar TFT pero el Jacko es mejor.')


async def setup(bot):
    await bot.add_cog(Basics(bot))
