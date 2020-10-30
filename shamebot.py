import os

import enum

import discord
from dotenv import load_dotenv


class BotIntensity(enum.Enum):
    loving_grandmother = 1
    positive_reinforcement = 2
    snarky_shame = 3
    moderate_shame = 4
    shame_lord = 5

class ShameBot(discord.ext.commands.Bot):
    intensity = BotIntensity.snarky_shame
