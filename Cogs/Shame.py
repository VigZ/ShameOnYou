import discord
from BotIntensity import ShameIntensity, EncouragementIntensity

class Shame(discord.commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.shame_intensity = ShameIntensity.snarky_shame


    @commands.command(name='shame', help='Shame your fellow group members for not being productive.')
    async def shame_user(self, ctx, *, member: discord.Member = None):
        """Shames a particular user."""
        choice = random.choice(SHAME_QUIPS[shame_bot.intensity])
        response = f'{member.mention} {choice}'
        await ctx.send(response)


    @shame_user.error
    async def shame_user_error(ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('I can\'t seem to find that user...')


    @commands.command(name='intensity', help='Change the bot\'s intensity 1-5.')
    async def change_intensity(ctx, intensity: int):
        if intensity < 0 or intensity > len(BotIntensity):
            raise commands.BadArgument

        shame_bot.intensity = BotIntensity(intensity)
        response = f'Intensity has been changed to {shame_bot.intensity.name}'
        await ctx.send(response)

    @change_intensity.error
    async def shame_user_error(ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('Please enter a level between 1 and 5.')

    @command.command(name='currentintensity', help='Gives the current shame intensity of Bot.')
    async def current_intensity(ctx):
        response = f'The current intensity is {shame_bot.intensity.name}'
        await ctx.send(response)
