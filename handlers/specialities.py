import asyncio

from disnake import Client, Interaction
from handlers.handler import Handler
from models.node import Node

tree = Node()


async def tree_start(client: Client, inter: Interaction):
    await inter.response.send_message(
        'Vous vous apprêtez à faire un test qui peut durer jusqu\'à 5 minutes. Voulez-vous continuer ?')
    message = await inter.original_message()
    await message.add_reaction('👍')
    await message.add_reaction('👎')

    def check(reaction, user):
        return user == inter.user and reaction.emoji in ['👍', '👎']

    try:
        reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
    except asyncio.TimeoutError:
        await tree['start']['cancel'](client, inter)
    else:
        if reaction.emoji == '👍':
            await tree['start']['continue'](client, inter)
        else:
            await tree['start']['cancel'](client, inter)


async def tree_continue(client: Client, inter: Interaction):
    await inter.followup.send('Le test va commencer dans quelques secondes.')
    await asyncio.sleep(5)
    await tree['start']['continue']['type'](client, inter)


async def tree_cancel(client: Client, inter: Interaction):
    await inter.followup.send('Vous avez choisi de ne pas continuer.')


async def tree_type(client: Client, inter: Interaction):
    message = await inter.followup.send('Vous considérez-vous plutôt littéraire ou scientifique ? 1️⃣ Littérature, '
                                        '2️⃣ Science')
    await message.add_reaction('1️⃣')
    await message.add_reaction('2️⃣')

    def check(reaction, user):
        return user == inter.user and reaction.emoji in ['1️⃣', '2️⃣']

    try:
        reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
    except asyncio.TimeoutError:
        await tree['start']['continue']['type']['scientist']['physic'](client, inter)
    else:
        if reaction.emoji == '1️⃣':
            await tree['start']['continue']['type']['literary'](client, inter)
        else:
            await tree['start']['continue']['type']['scientist'](client, inter)


async def tree_scientist(client: Client, inter: Interaction):
    message = await inter.followup.send('Êtes-vous rigoureux ? 1️⃣ Oui, 2️⃣ Non')
    await message.add_reaction('1️⃣')
    await message.add_reaction('2️⃣')

    def check(reaction, user):
        return user == inter.user and reaction.emoji in ['1️⃣', '2️⃣']

    try:
        reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
    except asyncio.TimeoutError:
        await tree['start']['continue']['type']['scientist']['physic'](client, inter)
    else:
        if reaction.emoji == '1️⃣':
            await tree['start']['continue']['type']['scientist']['physic'](client, inter)
        else:
            await tree['start']['continue']['type']['scientist']['nsi'](client, inter)


async def tree_literary(client: Client, inter: Interaction):
    message = await inter.followup.send('Préférez-vous le droit ou la lettre ? 1️⃣ Droit, 2️⃣ Littérature')
    await message.add_reaction('1️⃣')
    await message.add_reaction('2️⃣')

    def check(reaction, user):
        return user == inter.user and reaction.emoji in ['1️⃣', '2️⃣']

    try:
        reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
    except asyncio.TimeoutError:
        await tree['start']['continue']['type']['literary']['philosophy'](client, inter)
    else:
        if reaction.emoji == '1️⃣':
            await tree['start']['continue']['type']['literary']['philosophy'](client, inter)
        else:
            await tree['start']['continue']['type']['literary']['hggsp'](client, inter)


async def tree_physic(client: Client, inter: Interaction):
    await inter.followup.send('Puisque vous êtes rigoureux, nous vous conseillons de faire la spécialité '
                              'physique-chimie')
    await tree['start']['end'](client, inter)


async def tree_nsi(client: Client, inter: Interaction):
    await inter.followup.send('Puisque vous n\'êtes pas rigoureux, nous vous conseillons de faire la spécialité NSI')
    await tree['start']['end'](client, inter)


async def tree_hggsp(client: Client, inter: Interaction):
    await inter.followup.send('Puisque vous préférez le droit, nous vous conseillons de faire la spécialité '
                              'histoire-géo, géopolitique et sciences politiques')
    await tree['start']['end'](client, inter)


async def tree_philosophy(client: Client, inter: Interaction):
    await inter.followup.send('Puisque vous préférez la lettre, nous vous conseillons de faire la spécialité '
                              'philosophie')
    await tree['start']['end'](client, inter)


async def tree_end(client: Client, inter: Interaction):
    await inter.followup.send('Merci d\'avoir fait le test !')


tree.add_child(Node(tree_start, 'start'))
tree['start'].add_child(Node(tree_continue, 'continue'))
tree['start'].add_child(Node(tree_cancel, 'cancel'))
tree['start']['continue'].add_child(Node(tree_type, 'type'))
tree['start']['continue']['type'].add_child(Node(tree_scientist, 'scientist'))
tree['start']['continue']['type'].add_child(Node(tree_literary, 'literary'))
tree['start']['continue']['type']['scientist'].add_child(Node(tree_physic, 'physic'))
tree['start']['continue']['type']['scientist'].add_child(Node(tree_nsi, 'nsi'))
tree['start']['continue']['type']['literary'].add_child(Node(tree_hggsp, 'hggsp'))
tree['start']['continue']['type']['literary'].add_child(Node(tree_philosophy, 'philosophy'))
tree['start'].add_child(Node(tree_end, 'end'))


class SpecialitiesHandler(Handler):
    def __init__(self):
        self.state = {}

    @staticmethod
    async def start_form(inter):
        await tree['start'](inter.bot, inter)

    @staticmethod
    def setup():
        SpecialitiesHandler()
