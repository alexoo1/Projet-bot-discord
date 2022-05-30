import disnake
from disnake.ext import commands

intents = disnake.Intents.all()

bot = commands.Bot(intents=intents)


@bot.event
async def on_ready():
    print("The bot is ready!")
