import discord, os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'O {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("'ping"):
        await message.channel.send('pong!')
        
client.run(os.getenv('TOKEN'))
