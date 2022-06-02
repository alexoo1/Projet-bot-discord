from bot import bot
from commands.command import Command
from handlers.delete import DelHandler


class DelCommand(Command):
    def __init__(self):
        pass

    @bot.slash_command()
    async def delete(self, inter, i: int):
        await DelHandler.delete(inter, i)

    @staticmethod
    def setup():
       DelCommand()