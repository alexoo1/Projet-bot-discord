from bot import bot
from dotenv import load_dotenv
import os
from commands.delete import DelCommand
from commands.ping import PingCommand
from commands.pomodoro import PomodoroCommand
from commands.specialities import SpecialitiesCommand
from handlers.hello import HelloHandler
from commands.translate import TranslateCommand

load_dotenv()

PingCommand.setup()
HelloHandler.setup()
PomodoroCommand.setup()
SpecialitiesCommand.setup()
DelCommand.setup()
TranslateCommand.setup()

bot.run(os.getenv("DISCORD_BOT_TOKEN"))
