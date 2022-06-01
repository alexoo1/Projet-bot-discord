from bot import bot
from dotenv import load_dotenv
import os
from commands.ping import PingCommand
from handlers.hello import HelloHandler
from commands.translate import TranslateCommand

load_dotenv()

PingCommand.setup()
HelloHandler.setup()
TranslateCommand.setup()

bot.run(os.getenv("DISCORD_BOT_TOKEN"))
