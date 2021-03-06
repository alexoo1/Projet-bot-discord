import disnake
from disnake.ext import commands

intents = disnake.Intents.all()

bot = commands.Bot(intents=intents)


@bot.event
async def on_ready():
    print("The bot is ready!")


@bot.event
async def on_member_join(member):
    channel = disnake.utils.get(member.guild.channels, name="general")
    await channel.send(f"Bienvenue sur le serveur {member.display_name} !")


@bot.event
async def on_member_remove(member):
    channel = disnake.utils.get(member.guild.channels, name="general")
    await channel.send(f"Au revoir {member.display_name} !")
