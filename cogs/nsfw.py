import discord
from discord.ext import commands


class AnimeNSFW(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


  @commands.command(
    name="hentai",
    help="Displays NSFW anime."
  )
  @commands.is_nsfw() # command can only be used if channel = NSFW
  async def hentai_(self, ctx: commands.Context)
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://shiro.gg/api/images/hentai') as r:
        res = await r.json()
        embed = discord.Embed(
         color=discord.Colour.random()
         )
        embed.set_image(url=res['url'])
        await ctx.reply(embed=embed)

  @commands.command(
    name="thighs",
    help="Displays NSFW anime."
  )
  @commands.is_nsfw() # command can only be used if channel = NSFW
  async def thigh(self, ctx: commands.Context)
    async with aiohttp.ClientSession() as cs:
      async with cs.get('https://shiro.gg/api/images/thighs') as r:
        res = await r.json()
        embed = discord.Embed(
         color=discord.Colour.random()
         )
        embed.set_image(url=res['url'])
        await ctx.reply(embed=embed)



def setup(bot):
  bot.add_cog(AnimeNSFW(bot))
