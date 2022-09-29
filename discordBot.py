from pyexpat.errors import messages
import nextcord, datetime , asyncio
from nextcord.ext import commands
import logging                 #for logging errors
logging.basicConfig(level=logging.INFO)

import random
#intents setup
intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True
 
tarot = ['The Fool',
'The Magician',
'The High Priestess',
'The Empress',
'The Emperor',
'The High Priest',
'The Lovers','The Chariot','Strength','The Hermit',
'Wheel of Fortune','Justice','The Hanged Man','Death',
'Temperance','The Devil','The Tower','The Star','The Moon',
'The Sun','Judgement','The World']

bot = commands.Bot(command_prefix="$", intents=intents)

TESTING_GUILD_ID = 813117325166247998 #server id
bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await schedule_daily_message()

@bot.slash_command(name = "killthislove" , description= "To kill This love" , guild_ids=[TESTING_GUILD_ID])
async def hello(interaction: nextcord.Interaction):
    await interaction.send("Hello Bitch!")

@bot.slash_command(name = "dailytarot" , description = "A daily tarot Card for J")
async def tarotfunc(interaction: nextcord.Interaction):
    current_date = datetime.datetime.now().date()
    #current_date = current_date + datetime.timedelta(days = 15 )
    randominteger = 'jigyasa' + str(current_date)
    newint = 0

    for c in randominteger:
        newint = newint + int(ord(c))
    
    random.seed(newint)

    newint = random.randint(0,21)
    await interaction.send(tarot[newint])

#daily message scheduler
async def schedule_daily_message():
    
    while True:
        now = datetime.datetime.now()
        then = now + datetime.timedelta(minutes=1)
        wait_time = (then-now).total_seconds()
        await asyncio.sleep(delay = wait_time )

        channel = bot.get_channel(1023940215095701626)
        if(True):
            print(then, then.isoweekday() )
            await channel.send(f"Test Message {then} {then.isoweekday()}")
        
        

bot.run('MTAyMzg5MDIyMjYxMTcwMTgwMQ.GJ0YpO.cRu0W8bGIGapmKpYLBP3HvKlfeP1yjrj-AfkHI')
