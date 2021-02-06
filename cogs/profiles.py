import discord
from discord.ext import commands
import requests
import aiohttp


class AnimeProfiles(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(
    name="avatar",
    help="Generate an anime avatar.",
  )
  async def avatar_(self, ctx: commands.Context):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://shiro.gg/api/images/avatars') as r:
        res = await r.json()
        embed = discord.Embed(
         description=f"**Here's your anime avatar!**",
         color=discord.Colour.random()
         )
        embed.set_image(url=res['url'])
        await ctx.reply(embed=embed)

  @commands.command(
    name="wallpaper",
    help="Generate an anime wallpaper.",
  )
  async def wallpaper_(self, ctx: commands.Context):
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://shiro.gg/api/images/wallpapers') as r:
        res = await r.json()
        embed = discord.Embed(
          description=f"**Here's your wallpaper!**",
          color=discord.Colour.random()
        )
        embed.set_image(url=res['url'])
        await ctx.reply(embed=embed)




# More will be added soon! 

def setup(bot):
  bot.add_cog(AnimeProfiles(bot))
