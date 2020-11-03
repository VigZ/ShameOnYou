import discord
import discord.ext.commands as commands
import asyncio
import random

from BotIntensity import ShameIntensity, EncouragementIntensity
from quips import SHAME_QUIPS

import constants


class Shame(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.shame_intensity = ShameIntensity.snarky_shame


    @commands.command(name='shame', help='Shame your fellow group members for not being productive.')
    async def shame_user(self, ctx, member: discord.Member):
        """Shames a particular user."""
        choice = random.choice(SHAME_QUIPS[self.shame_intensity])
        response = f'{member.mention} {choice}'
        await ctx.send(response)


    @shame_user.error
    async def shame_user_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('I can\'t seem to find that user...')
        else:
            await ctx.send('Something strange is afoot...')


    @commands.command(name='shameintensity', help='Change the bot\'s intensity 1-5.')
    async def change_intensity(self, ctx, intensity: int):
        if intensity < 0 or intensity > len(ShameIntensity):
            raise commands.BadArgument

        self.shame_intensity = ShameIntensity(intensity)
        response = f'Intensity has been changed to {self.shame_intensity.name}'
        await ctx.send(response)

    @change_intensity.error
    async def change_intensity_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('Please enter a level between 1 and 5.')

    @commands.command(name='showshameintensity', help='Gives the current shame intensity of Bot.')
    async def current_intensity(self, ctx):
        response = f'The current intensity is {self.shame_intensity.name}'
        await ctx.send(response)

    @commands.command(name='shamecorner', help='Sends a particular user to the shame corner with the bot.')
    async def send_to_shame_corner(self, ctx, member: discord.Member):
        voice_channel_list = ctx.guild.voice_channels
        channel = discord.utils.find(lambda c: c.name == f'{constants.SHAME_CORNER_CHANNEL_NAME}', voice_channel_list)
        # Find specific channel for the shame corner.
        if channel is not None:
            vc = await channel.connect()
            #Pull targeted user to channel if they are in voice channel.
            await member.move_to(channel, reason="SHAME TIME")
            vc.volume = 1.0
            vc.play(discord.FFmpegPCMAudio('Audio/got-shame.mp3'), after=lambda e: print('done', e))
            while vc.is_playing():
                if member.voice.channel != channel:
                    await member.move_to(channel, reason="WHERE ARE YOU GOING")
                await asyncio.sleep(1)
            # # disconnect after the player has finished
            vc.stop()
            await vc.disconnect()
