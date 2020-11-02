import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv
from shamebot import BotIntensity, ShameBot
from quips import SHAME_QUIPS

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

shame_bot = ShameBot(command_prefix="!")

@shame_bot.event
async def on_ready():
    print(f'{shame_bot.user.name} has connected to Discord! Prepare for SHAME!')

@shame_bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hello {member.name}, welcome to {GUILD}! \n My name is ShameBot, let\'s keep eachother accountable, and be productive! \n Remember, I am always watching....'
    )


@shame_bot.command(name='shame', help='Shame your fellow group members for not being productive.')
async def shame_user(ctx, member: discord.Member):
    choice = random.choice(SHAME_QUIPS[shame_bot.intensity])
    response = f'{member.mention} {choice}'
    await ctx.send(response)

@shame_user.error
async def shame_user_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('I can\'t seem to find that user...')

@shame_bot.command(name='intensity', help='Change the bot\'s intensity 1-5.')
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

@shame_bot.command(name='currentintensity', help='Gives the current intensity of ShameBot.')
async def current_intensity(ctx):
    response = f'The current intensity is {shame_bot.intensity.name}'
    await ctx.send(response)

shame_bot.run(TOKEN)
