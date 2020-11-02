import discord
import discord.ext.commands as commands
from BotIntensity import ShameIntensity, EncouragementIntensity
from quips import ENCOURAGEMENT_QUIPS

import random

class Encouragement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.encouragement_intensity = EncouragementIntensity.empowering


    @commands.command(name='encourage', help='Encourage your group members into being the best they can be!.')
    async def encourage_user(self, ctx, member: discord.Member):
        """Shames a particular user."""
        choice = random.choice(ENCOURAGEMENT_QUIPS[self.encouragement_intensity])
        response = f'{member.mention} {choice}'
        await ctx.send(response)


    @encourage_user.error
    async def encourage_user_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('I can\'t seem to find that user...')
        else:
            await ctx.send('Something strange is afoot...')


    @commands.command(name='encouragementintensity', help='Change the bot\'s intensity 1-5.')
    async def change_intensity(self, ctx, intensity: int):
        if intensity < 0 or intensity > len(EncouragementIntensity):
            raise commands.BadArgument

        self.encouragement_intensity = EncouragementIntensity(intensity)
        response = f'Intensity has been changed to {self.encouragement_intensity.name}'
        await ctx.send(response)

    @change_intensity.error
    async def change_intensity_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('Please enter a level between 1 and 5.')

    @commands.command(name='showencouragementintensity', help='Gives the current encouragement intensity of Bot.')
    async def current_intensity(self, ctx):
        response = f'The current intensity is {self.encouragement_intensity.name}'
        await ctx.send(response)
