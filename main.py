import discord
from discord.ext import commands
from utils.shard import Bot
import os
from os import environ

bot = Bot(
    command_prefix=environ.get("DISCORD_PREFIX"), prefix=environ.get("DISCORD_PREFIX"),
    developer_ids=environ.get("DEVELOPERS"), command_attrs=dict(hidden=True), intents=discord.Intents(
        guilds=True, members=True, messages=True, reactions=True, presences=True
    ), allowed_mentions=discord.AllowedMentions(roles=False, users=True, everyone=False)
)
bot.help_command = commands.MinimalHelpCommand()


for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")


@bot.command(aliases=["src"])
async def source(ctx):
    await ctx.send("This bot was made with https://github.com/elfq/anime.py, and https://shiro.gg!")
# You're not allowed to remove this command by LICENSE, please review https://github.com/elfq/anime.py/blob/main/LICENSE for more information!
        
@bot.event 
async def on_ready():
  print("-----------")
  print(f"ID: {bot.user.id}")
  print(f"Username: {bot.user.name}")
  print("-----------")

bot.run(environ.get("DISCORD_TOKEN"))

# Step on the Scarlet Soil, Kamoking - Calm BGM
