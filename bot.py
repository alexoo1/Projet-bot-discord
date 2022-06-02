import disnake
from disnake.ext import commands

intents = disnake.Intents.all()

bot = commands.Bot(intents=intents)


@bot.event
async def on_ready():
    print("The bot is ready!")


@bot.event
async def on_member_join(member):
    general_channel = bot.get_channel(979421769284878408)
    await general_channel.send(f"Bienvenue sur le serveur {member.display_name} !")
