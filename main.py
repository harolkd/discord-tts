import discord, asyncio, os
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
load_dotenv()

bot = commands.Bot(command_prefix="'", description="Discord tts bot core", intents=intents)

async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    await load_extensions()
    await asyncio.sleep(1)
    return
    
asyncio.run(main())
bot.run(os.getenv('TOKEN'))
