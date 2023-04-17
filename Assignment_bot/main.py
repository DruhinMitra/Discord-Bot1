import discord 
from discord import app_commands
from discord.ext import commands

TOKEN=''

# added test comment

bot=commands.Bot(command_prefix='/',intents=discord.Intents.all())

@bot.event
async def on_ready():
    
    print("BOT READY")
    try:
        sync=await bot.tree.sync()
        
    except Exception as e:
        print("ERROR",e)
        
@bot.tree.command(name='suckmypp')                            # have fun with this if u r single . Will later on add the sound too :)
async def suckmypp(Intr):
    await Intr.response.send_message('GWAK GWAK X3000')


        


@bot.tree.command(name='assingment')
@app_commands.describe(p="Topics of physics")
@app_commands.describe(m="Topics of Maths")
@app_commands.describe(c="Topics of Chemistry")
@app_commands.describe(t="Enter the time(in hours)")
async def assignment(Intr,p:str,m:str,c:str,t:str):                            #This is the assignment function that will take the assignments from user
    tasks = [p, c, m]
    if tasks:
        
      
        await Intr.response.send_message(f'Your to-do list:\n{tasks}\n complete it under {t} hours \n ALL THE BEST')
    else:
        print("empty")
      
        await Intr.response.send_message('Your to-do list is empty!')

    
    
    






    
bot.run(TOKEN) #Enter yout discord token
    
