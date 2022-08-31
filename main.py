import discord, asyncio, os, json
from discord.ext import commands
from dotenv import load_dotenv
from functions import setupFiles

intents = discord.Intents.default()
data = json.load(open('config.json'))

intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=data['prefix'], description=data['description'], intents=intents)

async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    await load_extensions()
    return
    
if __name__ == "__main__":
    load_dotenv()
    setupFiles()
    asyncio.run(main())
    bot.run(os.getenv('TOKEN'))
