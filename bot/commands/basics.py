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

    @commands.command()
    async def gino(self, ctx):
        user = await self.bot.fetch_user('468960837365661716')
        await ctx.send(f'{user.mention} es un master del Wildrift y del Ballorant. Lamentablemente no juega TFT ya que dice que es un juego muy fácil para el.')

    @commands.command()
    async def chesqo(self, ctx):
        user = await self.bot.fetch_user('566528150826385409')
        await ctx.send(f'{user.mention} es dueño y amo del servidor, sin él yo no existiera. Entre sus habilidades especiales se encuentra quejarse del lag todo el momento.')

    @commands.command()
    async def overkill(self, ctx):
        user = await self.bot.fetch_user('248689889355366400')
        await ctx.send(f'{user.mention} posiblemente el mejor midlaner del servidor después de Moonify. Le gusta el rammen, el anime, leer y escribir. Cuenta la leyenda que mi primera versión fue creada por él y Moonify, luego se aburrio y me dejo en el abandono.')

    @commands.command()
    async def jacko(self, ctx):
        user = await self.bot.fetch_user('250473528485347328')
        await ctx.send(f'{user.mention} el nuevo amo y dueño del server. Entre sus habilidades esta ser el mejor Swain del mundo y coger aumentos de mierda en el TFT. ')

    @commands.command()
    async def tevi(self, ctx):
        user = await self.bot.fetch_user('468961042832293908')
        await ctx.send(f'{user.mention} de nacionalidad mexicana, es el mejor ADC del servidor. Entre sus habilidades esta echarle la culpa al jungla cuando pierde bot con el Jacko.')

    @commands.command()
    async def yormom(self, ctx):
        user = await self.bot.fetch_user('460869447201325056')
        await ctx.send(f'{user.mention} fancito de T1 de corazón y la mejor poppy de LAN. A ratos le da por trolear jugando Azir mid, al igual que Gino, no juega TFT porque dice que es muy fácil para él :).')

    @commands.command()
    async def moonify(self, ctx):
        user = await self.bot.fetch_user('441435704942133249')
        await ctx.send(f'{user.mention}/mancofy mi amo y creador, con el nada me falta. Entre sus habilidades esta ser el mejor jungla del servidor y el mejor jugador de TFT. Su counter natural es stiwers quien con su juego inpensante deja en jaque a Moonify.')

    @commands.command()
    async def mishi(self, ctx):
        user = await self.bot.fetch_user('643117585847549962')
        await ctx.send(f'{user.mention} es el infame del servidor. Su aporte a la jungla y los cortes de luz durante los clash son invaluables entre los que lo conocen en el servidor.')

    @commands.command()
    async def karurosu(self, ctx):
        user = await self.bot.fetch_user('383093792892256256')
        await ctx.send(f'{user.mention} o mejor dicho el Caluroso, poco a poco se convirtio en el mas mandarina del servidor. Lo cierto es que nos ha dejado a la deriva, pero siempre lo recordaremos por sus frases celebres como: "Coma mierda Pozo".')

async def setup(bot):
    await bot.add_cog(Basics(bot))
