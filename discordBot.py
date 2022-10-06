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

eventlist = [                                                          #EVENT NAME LIST
              [#hour , #minute , #dayofweek , #event name],
              [#hour , #minute , #dayofweek , #event name],
              [#hour , #minute , #dayofweek , #event name],
              [#hour , #minute , #dayofweek , #event name],
               -------------------------------------------
               -------------------------------------------
            ]

bot = commands.Bot(command_prefix="$", intents=intents)

TESTING_GUILD_ID =  ####### #server id
bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await schedule_daily_message()

#Daily Tarot Card
@bot.slash_command(name = "dailytarot" , description = "Enter your first name to get a Tarot Card")
async def tarotfunc(interaction: nextcord.Interaction , name : str ):
    current_date = datetime.datetime.now().date()
    #current_date = current_date + datetime.timedelta(days = 15 )
    name = name.lower()
    randominteger = name + str(current_date)
    newint = 0

    for c in randominteger:
        newint = newint + int(ord(c))
    
    random.seed(newint)

    newint = random.randint(0,21)
    filename = "Tarot\\" + str(newint) + '.jpg'
    await interaction.send(f"Hi {name}, your tarot card for {current_date} is {tarot[newint]}" , file=nextcord.File(filename))

#daily message scheduler
async def schedule_daily_message():
    
    while True:
        now = datetime.datetime.now()
        then = now + datetime.timedelta(seconds=5)
        wait_time = (then-now).total_seconds()
        await asyncio.sleep(delay = wait_time )

        channel = bot.get_channel("Target Channel int")
        
        for lis in eventlist:
            weekday = then.isoweekday()
            if  lis[2] == weekday or lis[2] == -1:
                if(then.hour == lis[0] and then.minute == lis[1]):
                    await channel.send(f"Hi Friend! Its {then.hour}:{then.minute}, time for {lis[3]}")
                    await asyncio.sleep(delay = 60)
        
        

bot.run('YOUR BOT TOKEN')   
