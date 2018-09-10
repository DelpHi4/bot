import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("?", "!")

client = Bot(command_prefix=BOT_PREFIX)

@client.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])
        
@client.command(name='Шар',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['Шарик', '8Шарик', '8Шар', 'шар', '8шарик', '8шар', 'ШАРИК', '8ШАРИК', '8ШАР', 'ШАР'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'Определённо нет',
        'Вероятно, нет',
        'Сложно сказать',
        'Возможно',
        'Определённо да',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)
    
    
@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Хейтер Витали", description="Топ бот ин зе ворлд", color=0xeee657)
    
    # give info about you here
    embed.add_field(name="Author", value="<DelphinG3>")
    
    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="[Invite link](<https://discordapp.com/oauth2/authorize?client_id=485503349517713418&scope=bot&permissions=2146958847>)")

    await ctx.send(embed=embed)
    
@client.command()
async def квадрат(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " В квадрате " + str(squared_value))


client.run("NDg1NTAzMzQ5NTE3NzEzNDE4.Dm0jJw.RjBFbnkIQEcPE-zpP6EHTyquzoQ")
