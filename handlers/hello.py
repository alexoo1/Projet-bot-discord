from bot import bot
from handlers.handler import Handler


class HelloHandler(Handler):
    def __init__(self):
        self.state = {}

    async def hello(self, message):
        if message.author.id == bot.user.id:
            return

        if message.content.lower() == "hello":
            await message.reply("Hello!")

    @staticmethod
    def setup():
        handler = HelloHandler()

        bot.add_listener(handler.hello, "on_message")
