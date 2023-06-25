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
        user = await self.bot.fetch_user('703721870482079834')
        await ctx.send(f'{user.mention} es un jugador main Diana, que se dedica a trolear partidas en MID. También de vez en cuando se dedica a jugar TFT pero el Jacko es mejor.')

    @commands.command()
    async def microrocket(self, ctx):
        user = await self.bot.fetch_user('249434388167655435')
        await ctx.send(f'{user.mention} alias MarcoManco es el mejor jugador de Volibear en todo el mundo. A veces también juega TFT pero es un manco de mierda.')

    @commands.command()
    async def stiwers(self, ctx):
        user = await self.bot.fetch_user('548529415055998988')
        await ctx.send(f'{user.mention} es un manco de mierda, no hace falta decir mas.')

async def setup(bot):
    await bot.add_cog(Basics(bot))
