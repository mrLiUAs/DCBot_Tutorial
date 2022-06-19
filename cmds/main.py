import discord
from discord.ext import commands
import os
from core import Cog_Extension


class Main(Cog_Extension):

    @commands.command()
    async def Hello(self, ctx):
        await ctx.send(f"Hello, {ctx.author} in {ctx.channel}")

    @commands.command()
    async def meme(self, ctx):
        embed=discord.Embed(title="這是我的作業", url="https://memeprod.sgp1.digitaloceanspaces.com/user-wtf/1655613760823.jpg", description="實際上的樣子", color=0xbe38f3)
        embed.set_author(name="Xavier", url="https://memes.tw/wtf?template=23259", icon_url="https://memeprod.ap-south-1.linodeobjects.com/user-template/2b32d29ba9dbba00a8b8d24508dd77e6.png")
        embed.add_field(name="undefined", value="undefined", inline=False)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def Video(self,ctx):
        embed=discord.Embed(title="杰哥不要 the 音樂劇", url=os.getenv("title"), description="非常好影片", color=0xce1c1c)
        embed.set_author(name="杰哥", url=os.getenv("author"), icon_url=os.getenv("icon"))
        embed.set_thumbnail(url=os.getenv("thumbnail"))
        await ctx.send(embed=embed)

    @commands.command()
    async def bullshit(self, ctx):
        await ctx.send(crawler.getBullShit(topic='齜牙', length=100))

def setup(bot):
    bot.add_cog(Main(bot))