# Hanging Out In Tokyo, Meesan - Calm BGM

# Backwater, Kamoking - Battle BGM

# Storm Spirit, Kamoking - Battle BGM

# Winter Satellite, Sudo Mikaduki - Calm BGM

# Samurai Sword, Kamoking - Battle BGM

import discord
from discord.ext import commands
import requests
import aiohttp


class AnimeGifs(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(
    name="hug",
    help="Hug a user! (or yourself :D)",
    usage="@elf#1000"
  )
  async def hug_(self, ctx: commands.Context, user : discord.Member):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://shiro.gg/api/images/hug') as r:
        res = await r.json()
        if user == ctx.author: # Checks if command user is themselves.
         embed = discord.Embed(
           description=f"**{ctx.author.name}** hugs themselves!",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)
        else: 
         embed = discord.Embed(
           description=f"**{ctx.author.name}** hugs **{user.name}**",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)

  @commands.command(
    name="kiss",
    help="Kiss a user! (or yourself (somehow))",
    usage="@elf#1000"
  )
  async def kiss_(self, ctx: commands.Context, user : discord.Member):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://shiro.gg/api/images/kiss') as r:
        res = await r.json()
        if user == ctx.author: # Checks if command user is themselves.
         embed = discord.Embed(
           description=f"**{ctx.author.name}** kisses themselves (i guess?)",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)
        else: 
         embed = discord.Embed(
           description=f"**{ctx.author.name}** kisses **{user.name}**",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)

  @commands.command(
    name="pat",
    help="Give a pat to yourself or others!",
    usage="@elf#1000"
  )
  async def pat_(self, ctx: commands.Context, user : discord.Member):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://shiro.gg/api/images/pat') as r:
        res = await r.json()
        if user == ctx.author: # Checks if command user is themselves.
         embed = discord.Embed(
           description=f"**{ctx.author.name}** gives themselves a pat on the back!",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)
        else: 
         embed = discord.Embed(
           description=f"**{ctx.author.name}** pats **{user.name}**",
           color=discord.Colour.random()
         )
         embed.set_image(url=res['url'])
         await ctx.reply(embed=embed)


# More will be added soon! 

def setup(bot):
  bot.add_cog(AnimeGifs(bot))
