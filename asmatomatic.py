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