from dis import disco
from distutils import core
from re import L
import discord
from discord.ext import commands
import os
from core import Cog_Extension

from feature import meme, todo
# data(s)
ppl = 0
schedule = {}
todo_msg_id = None
#

class Main(Cog_Extension):

    @commands.command()
    async def Hello(self, ctx):
        await ctx.send(f"Hello, {ctx.author} in {ctx.channel}")

    @commands.command()
    async def todo(self, ctx, method, time, content):
        #methods
        if method == "add":
            #basic bug avoiding
            if len(time.split('/')) != 3:
                await ctx.send("The format should be: $todo add <YYYY/MM/DD> <content>")
            else:
                global schedule
                _date = tuple(map(int, time.split('/')))
                schedule = todo.addEvent(schedule, _date, content)
                global todo_msg_id

                embed=discord.Embed(title="TODO-list", description="a list in which contains your schedule(as it says)")
                for key, value in schedule.items():
                    embed.add_field(name=f"{key.year}/{key.month}/{key.day}", value=value, inline=False)
                if todo_msg_id:
                    msg = await ctx.fetch_message(todo_msg_id)
                    await msg.edit(embed=embed)
                else:
                    todo_embed = await ctx.send(embed=embed)
                    todo_msg_id = todo_embed.id

    @commands.command()
    async def aabb(self, ctx):
        await ctx.send("Feature Developing!")
    @commands.command()
    async def meme(self, ctx):
        await ctx.send(meme.getMeme())
    @commands.command()
    async def stonk(self, ctx):
        await ctx.send("Feature Developing!")
    @commands.command()
    async def test(self, ctx):
        global ppl
        try:
            ppl += 1
        except:
            ppl = 1
        await ctx.send(ppl)

    @commands.command()
    async def test1(self, ctx):
        msg = await ctx.fetch_message(ctx.id)
        await msg.edit(content= 'Hi1')
    
    @commands.command()
    async def test2(self, ctx):
        channel = commands.Bot.get_channel(992102936572350507)
        await channel.send('hithere')
    

def setup(bot):
    bot.add_cog(Main(bot))