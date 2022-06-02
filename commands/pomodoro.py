from bot import bot
from commands.command import Command
from handlers.pomodoro import PomodoroHandler

pomodoro_handler_instance = PomodoroHandler()


class PomodoroCommand(Command):
    def __init__(self):
        pass

    @bot.slash_command()
    async def pomodoro(self, inter):
        """Starts a pomodoro"""
        await pomodoro_handler_instance.timer(inter)

    @staticmethod
    def setup():
        PomodoroCommand()
