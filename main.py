# Library Imports
import nextcord, os
from nextcord.ext import commands
from dotenv import load_dotenv

# Custom Imports
from functions.main import loadup

# Bot Class / Object
class StartUp(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix = "/",
            case_insensitive = True,
            intents = nextcord.Intents.all()
        )

bot = StartUp()

# Loading Extentions
loadup(["plugins"], bot)

# Launch the bot
load_dotenv('.env')
bot.run(os.getenv("DiscordToken"))