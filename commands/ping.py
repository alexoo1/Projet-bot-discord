from bot import bot
from commands.command import Command
from handlers.ping import PingHandler


class PingCommand(Command):
    def __init__(self):
        pass

    @bot.slash_command()
    async def ping(self, inter):
        """Says pong"""
        await PingHandler.ping(inter)

    @staticmethod
    def setup():
        PingCommand()
