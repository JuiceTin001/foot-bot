import discord
from discord.ext import commands

class Functions(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is online")
    @commands.command()
    async def bye(self,ctx):
        await ctx.send("Bye")

    @commands.command()
    async def hello(self,ctx):
        await ctx.send("Hey there!")

    @commands.command()
    async def Clear(self,ctx,amount=10+1):
        await ctx.channel.purge (limit = amount)
        await ctx.send ("The messages has been cleared")

def setup(bot):
    bot.add_cog(Functions(bot))