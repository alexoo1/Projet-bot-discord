from bot import bot
from commands.command import Command
from handlers.specialities import SpecialitiesHandler


class SpecialitiesCommand(Command):
    def __init__(self):
        pass

    @bot.slash_command()
    async def specialities(self, inter):
        """Find the best speciality for you"""
        await SpecialitiesHandler.start_form(inter)

    @staticmethod
    def setup():
        SpecialitiesCommand()
