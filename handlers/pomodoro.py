import disnake

from bot import bot
from handlers.handler import Handler
import time
import asyncio


class PomodoroHandler(Handler):
    def __init__(self):
        self.state = {'pomodoro': {}}
        asyncio.ensure_future(self.__interval())

    async def __interval(self):
        now = time.time()
        for user_id, end_time in list(self.state['pomodoro'].items()):
            print(end_time - now)
            if end_time - now < 0:
                try:
                    await bot.get_user(user_id).send('Time for a break!')
                except disnake.errors.HTTPException:
                    try:
                        guild = bot.get_user(user_id).mutual_guilds[0]
                        if guild is None:
                            continue
                        await disnake.utils.get(guild.channels, name='general').send(f'Time for a break! '
                                                                                     f'@{bot.get_user(user_id).name}')
                    except Exception as e:
                        print(e)

                del self.state['pomodoro'][user_id]
        await asyncio.sleep(60)
        await self.__interval()

    async def timer(self, inter):
        if inter.author.id == bot.user.id:
            return

        self.state['pomodoro'][inter.author.id] = time.time() + 25 * 60
        await inter.response.send_message("Pomodoro started!")

    @staticmethod
    def setup():
        PomodoroHandler()
