###############################################################################
# asmatomatic
# ./asmatomatic.py
#
# Author: John C <https://lvl-6.github.io>
# Created: 27/10/2020
#
# Description:
# For when Asmat isn't around, the Asmatomatic will generate
# questions and tell you how to do things from class.
# Intended for students on the HNC Comp Tech/Comp Sci classes.
# Written by students, for students.
#
###############################################################################

import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot as BotBase

version = "0.0.1"
bot_token = os.getenv('ASMAT_TOKEN')

###############################################################################
# Bot Initialisation
###############################################################################

# We will load only the cogs in this list for security reasons.
extensions = ['cogs.conversions']

bot = BotBase(
    command_prefix = commands.when_mentioned,
    description = 'I generate questions and answers from Asmat\'s class',
    owner_ids = 0,
    case_insensitive = True,
    )

# Program is running as main (i.e. not imported by another program)
if __name__ == '__main__':
    for extension in extensions:
        bot.load_extension(extension)
        print('Loaded extension: ' + extension)
#TODO: Look into unloading these as well, so that they can have their own
#"mode" and I can have commands with the same name across the project.

@bot.event
async def on_connect():
    print('Connected to Discord...')

@bot.event
async def on_disconnect():
    print('Disconnected from Discord...')

@bot.event
async def on_ready():
    print('Online and Ready!')
    
###############################################################################
# Program Execution
###############################################################################

bot.run(bot_token)