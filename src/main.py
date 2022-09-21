from discord.ext import commands
from discord.utils import get
import discord
import random


intents = discord.Intents.default()
intents.members = True
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
    await member.add_roles(role_admin)
    await ctx.send(f'WP {member}, you have been promoted to administrator')

token = ""
bot.run(token)  # Starts the bot