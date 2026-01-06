import discord
from discord.ext import commands
import json
import random
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

characters = []

for file in os.listdir("characters"):
    if file.endswith(".json"):
        with open(f"characters/{file}", "r", encoding="utf-8") as f:
            characters.extend(json.load(f))

@bot.event
async def on_ready():
    print(f"Bot online como {bot.user}")
    print(f"{len(characters)} personagens carregados")

@bot.command()
async def dex(ctx):
    char = random.choice(characters)

    embed = discord.Embed(
        title="📘 BFDI-DEX",
        description=f"**#{char['id']} — {char['name']} {char['emoji']}**",
        color=0x00CFFF
    )
    embed.add_field(name="Temporada", value=char["season"], inline=True)
    embed.add_field(name="Primeiro episódio", value=char["first_episode"], inline=True)
    embed.set_image(url=char["image"])

    await ctx.send(embed=embed)

bot.run(os.getenv("TOKEN"))

