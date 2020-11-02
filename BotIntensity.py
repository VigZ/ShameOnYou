import os

import enum

import discord
from dotenv import load_dotenv


class ShameIntensity(enum.Enum):
    diet_shame = 1
    light_shame = 2
    snarky_shame = 3
    moderate_shame = 4
    shame_lord = 5


class EncouragementIntensity(enum.Enum):
    light_encouragement = 1
    moderate_encourement = 2
    empowering = 3
    pregame_speech = 4
    speech_with_epic_music = 5
