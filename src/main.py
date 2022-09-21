from discord.ext import commands
from discord.utils import get
import discord
import random


intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 226250876338176002  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.event
async def on_message(msg):
    if msg.content == "Salut tout le monde":
        channel = msg.channel
        await channel.send('Salut tout seul')
    await bot.process_commands(msg)


@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.command()
async def name(ctx):
    await ctx.send(ctx.author)

@bot.command()
async def d6(ctx):
    pos = [1, 2, 3, 4, 5, 6]
    await ctx.send(random.choice(pos))

@bot.command()
async def admin(ctx, member: discord.Member):
    role_admin = None
    for role in member.guild.roles[1:]:     #get the admin role
        if role.name == "admin":
            role_admin = role

    if role_admin == None :
        perms = discord.Permissions(manage_channels=True, kick_members=True, ban_members=True)
        role_admin = await member.guild.create_role(name="admin", permissions=perms)
    elif role_admin in member.roles[1:]: 
        await ctx.send(f'{member} is already an administrator')
        return
    await member.add_roles(role_admin)
    await ctx.send(f'WP {member}, you have been promoted to administrator')

@bot.command()
async def ban(ctx, member: discord.Member,reason: str = "mérité"):
    await member.ban(reason=reason)
    await ctx.send(f'So long {member}')

@bot.command()
async def count(ctx):
    nb_off = 0
    nb_idle = 0
    nb_online = 0
    nb_dnd = 0

    for member in bot.get_all_members():
        if member.status.value == "offline" :
            nb_off+=1
        elif member.status.value == "online" :
            nb_online+=1
        elif member.status.value == "idle" :
            nb_idle+=1
        elif member.status.value == "dnd" :
            nb_dnd+=1

    await ctx.send(f'{nb_online} members are online, {nb_idle} are idle and {nb_off} are off')
    await ctx.send(f'And last but not least {nb_dnd} do not disturb')

@bot.command()
async def xkcd(ctx):
    id = random.randint(1,2673)  # why 2673 ? because it was the last one available (21/09/2022)
    await ctx.send(f'https://xkcd.com/{id}/')

token = ""
bot.run(token)  # Starts the bot