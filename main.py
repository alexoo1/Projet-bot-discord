from bot import bot
from dotenv import load_dotenv
import os
from commands.ping import PingCommand
from commands.pomodoro import PomodoroCommand
from handlers.hello import HelloHandler

load_dotenv()

PingCommand.setup()
HelloHandler.setup()
PomodoroCommand.setup()

bot.run(os.getenv("DISCORD_BOT_TOKEN"))
