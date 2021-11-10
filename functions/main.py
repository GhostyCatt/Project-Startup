# Library Imports
import os
from nextcord.ext import commands

# Custom Imports
from functions.logger import log

# Functions 
def loadup(folders: list[str], bot: commands.Bot):
    """Load all extentions into the bot"""
    log("INFO", "Starting to load extentions.")
    bot.load_extension("jishaku")
    for folder in folders:
        for item in os.listdir(f"{folder}/"):
            if item.endswith(".py"):
                try:
                    bot.load_extension(f"{folder}.{item[:-2]}")
                    log("LOAD", f"{folder}/{item} was loaded successfully!")
                except Exception as e:
                    log("LOAD", f"{folder}/{item} couldn't be loaded: \"{e.__cause__}\"")
    log("INFO", "Finished loading extentions.")