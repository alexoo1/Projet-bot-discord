from handlers.handler import Handler


class PingHandler(Handler):
    def __init__(self):
        self.state = {}

    @staticmethod
    async def ping(inter):
        await inter.response.send_message("Pong!")

    @staticmethod
    def setup():
        PingHandler()
