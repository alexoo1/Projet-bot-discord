from handlers.handler import Handler

class DelHandler(Handler):
    def __init__(self):
        self.state = {}

    @staticmethod
    async def delete(inter, i):
        number = int(i)
        messages = await inter.channel.history(limit=number).flatten()
        
        for each_message in messages:
            await each_message.delete()

        await inter.send('Les messages ont correctement été supprimés!✅')
