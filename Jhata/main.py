import discord 
from discord import app_commands
from discord.ext import commands
TOKEN='MTA5NjY3MTE1MDIxMTMzNDE3NA.G95T1W.p5iRLSO9undvwkvK_eO3D_5BBoOw-1wVDLMMEU'

# added test comment

bot=commands.Bot(command_prefix='/',intents=discord.Intents.all())

@bot.event
async def on_ready():
    
    print("BOT READY")
    try:
        sync=await bot.tree.sync()
        
    except Exception as e:
        print("ERROR",e)
        
@bot.tree.command(name='suckmypp')
async def suckmypp(Intr):
    await Intr.response.send_message('GWAK GWAK 3000')

@bot.event    
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith('!hello'):
        await message.channel.send('HELLOOOOO')
        # await Intr.response.send_message("Hellooo")
        
        
# @bot.event

@bot.tree.command(name='assingment')
@app_commands.describe(p="Topics of physics: ")
@app_commands.describe(m="Topics of Maths: ")
@app_commands.describe(c="Topics of Chemistry: ")


async def assingment(Intr,p:str,c:str,m:str):                           # This function will take assingment and the alloted time from user
    try:
        await Intr.response.send_message(p)
        await Intr.response.send_message(m)
        await Intr.response.send_message(c)
    except Exception as e:
        print("error",e)
    
    
    
bot.run(TOKEN)
    
