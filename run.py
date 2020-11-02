import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv
from BotIntensity import ShameIntensity
from quips import SHAME_QUIPS, ENCOURAGEMENT_QUIPS
from Cogs.Shame import Shame

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

accountability_bot = commands.Bot(command_prefix="!")
accountability_bot.add_cog(Shame(accountability_bot))

@accountability_bot.event
async def on_ready():
    print(f'{accountability_bot.user.name} has connected to Discord! Accountability engaged.')

@accountability_bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hello {member.name}, welcome to {GUILD}! \n My name is {accountability_bot.name}, let\'s keep eachother accountable, and be productive! \n Remember, I am always watching....'
    )


accountability_bot.run(TOKEN)
