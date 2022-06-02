from bot import bot
from dotenv import load_dotenv
import os
from commands.delete import DelCommand
from commands.ping import PingCommand
from handlers.hello import HelloHandler

load_dotenv()

PingCommand.setup()
HelloHandler.setup()
DelCommand.setup()

bot.run(os.getenv("DISCORD_BOT_TOKEN"))
