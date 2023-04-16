import discord 
from discord import app_commands
from discord.ext import commands
TOKEN='MTA5NjY3MTE1MDIxMTMzNDE3NA.GJr7YR.AepsGTNE4ozuiMDSO_ddGo2J9UkNoBKJ6tV5nQ'

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
@app_commands.describe(p="Topics of physics")
@app_commands.describe(m="Topics of Maths")
@app_commands.describe(c="Topics of Chemistry")
@app_commands.describe(t="Enter the time")

async def assingment(Intr,p:str,c:str,m:str):                           # This function will take assingment and the alloted time from user
    await Intr.response.send_message("Okay... all the best")
    
    
bot.run(TOKEN)
    
