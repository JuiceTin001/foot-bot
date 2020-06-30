import discord,os
from discord.ext import commands,tasks
from itertools import cycle

bot = commands.Bot(command_prefix = "[]")
status = cycle(["undertale","deltarune","fortnite","BloonsTD6"])

@bot.event
async def on_ready():
    change_status.start()
    print('Bot is ready')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    bot.load_extension(f"cogs.{extension}")

@tasks.loop(minutes = 10)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


bot.run("NzI3NDE5Njk1NTE4NDQ5NzA1.Xvrkaw.Zf3XLs5nWB6lKmHKm3iEKKp3-70")
