from discord import Embed
from discord.ext import commands
from utils.api import get_summoner_data

class TFTStats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def stats(self, ctx, name: str):
        try:
            data = await get_summoner_data(name)
            if data:
                data = data[0] 
                total_games = data['wins'] + data['losses']
                win_ratio = round((data['wins'] / total_games) * 100, 2)  # Win ratio as a percentage.

                embed = Embed(title=f"Estadísticas de {name}", color=0x3498db) # Creas un Embed con título y color.
                embed.add_field(name="Rango", value=f"{data['tier']} {data['rank']}", inline=True) # Agregas un campo al Embed.
                embed.add_field(name="Top 4", value=f"{data['wins']}", inline=True)
                embed.add_field(name="Total de partidas", value=f"{total_games}", inline=True)
                embed.add_field(name="Win Ratio", value=f"{win_ratio}%", inline=True)

                await ctx.send(embed=embed) # En lugar de enviar un mensaje de texto, envías el Embed.
        except Exception as err:
            print(err)
            await ctx.send("Lo siento algo salio mal. Revisa que el nombre de invocador sea correcto o comunicate con Moonify")

async def setup(bot):
    await bot.add_cog(TFTStats(bot))
