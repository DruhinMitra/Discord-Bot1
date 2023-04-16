import discord
from discord import app_commands
from discord.ext import commands

TOKEN = 'MTA5NjY2OTYzNjYxMjg3MDIwNQ.Gi65d8.6Z1AEDzH7blrB6YK8YkGJZWpgN0Qkfe9xL-Ezs'

# Create a Bot instance
bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

'''

in python we have function decoraters that I will cover later
for now think of it as a tag that would link all the functions with the bot instance we created

here you can see we have @bot.event decorator
this is used when we ar listening for events 

MORE ABOUT EVENTS here: 
https://discordpy.readthedocs.io/en/stable/api.html#event-reference

'''

@bot.event
async def on_ready():
    print("Bot ready")
    try:
        sync = await bot.tree.sync() # sync the commands
    except Exception as e:
        print("Error", e)


'''
here you can find bot.tree.command
the bot.tree is basically an array that holds all the commands that your bot will have...
thats why the decorator says bot.tree.command

these commands are to be registerd in your server... before using
that is why we wheren't getting the help message
for syncing these commands globally to all servers the bot is running on
we use

await bot.tree.sync()

down here you will find a function with decorator
the decorator takes in paramter like name, breif etc you can find them in documentation...

this is a simple function that prints Hello World
'''

# normal command
@bot.tree.command(name="hello")
async def hello(intr):
    await intr.response.send_message("Hello World")

'''
Now some functions we need paramaters for that we have to import the app_command moudule..
It might seem a bit confusing to use these decorators ..
but they are just tags.. dont get afraid by them

here we have tagged the function with app_command that represents that the function needs a given paramater
'''
# command with paramater(s)
@bot.tree.command(name="echo")
@app_commands.describe(msg = "message to echo")
@app_commands.describe(msg2 = "message 2 to echo")
async def echo(intr, msg : str, msg2: str):
    await intr.response.send_message(msg)
    await intr.response.send_message(msg2)


# start the bot
bot.run(TOKEN)