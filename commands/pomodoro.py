from bot import bot
from commands.command import Command
from handlers.pomodoro import PomodoroHandler
import time
import asyncio

class PomodoroCommand(Command):
    def __init__(self):
        self.state = {'pomodoro': {}}
        self.__interval()

    async def __interval(self):
        now = time.time()
        for user_id, end_time in self.state['pomodoro'].items():
            if end_time - now > 0:
                bot.get_user(user_id).send('Time for a break boss')
                del self.state['pomodoro'][user_id]
        await asyncio.sleep(60 * 5)          
        await self.__interval()

    @bot.slash_command()
    async def pomodoro():
        await PomodoroHandler.pomodoro()

    @staticmethod
    def setup():
        PomodoroCommand()