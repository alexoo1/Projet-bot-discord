from code import InteractiveConsole
from bot import bot
from handlers.handler import Handler
import time
import asyncio

class PomodoroHandler(Handler):
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
        #
        await self.__interval()

    async def timer(self, message):
        if message.author.id == bot.user.id:
            return    
            
        if message.content.isnumeric():
            self.state['pomodoro'][bot.user.id] = time.time() + 25 * 60