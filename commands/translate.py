from bot import bot
from commands.command import Command
from handlers.translate import TranslateHandler


class TranslateCommand(Command):
    def __init__(self):
        pass

    @bot.slash_command()
    async def translate(inter,lang_to:str ,text:str):
        """Traduire un texte"""
        await TranslateHandler.translate(inter,lang_to ,text)

    @staticmethod
    def setup():
        TranslateCommand()
