# bot.py
import math
import os

from dotenv import load_dotenv

from utils import get_fuel, get_number_of_laps

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

from discord.ext import commands

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    for guild in bot.guilds:
        print(guild.name)

    print(
        f"{bot.user} is connected to the following guild:\n"
        f"{guild.name}(id: {guild.id})"
    )


@bot.command(
    name="fuel",
    help="""jak używać bota:
    !fuel (czas wyścigu w minutach) (czas okrążenia) (spalanie)
    przykład: !fuel 24 2:25:2 3.42""",
)
async def fuel(ctx, duration: int, lap_time: str, fuel_per_lap: float):
    if ctx.author == bot.user:
        return
    nof_laps = get_number_of_laps(duration, lap_time)
    fuel = get_fuel(nof_laps, fuel_per_lap)
    response = (
        "<@{author}>, Wynik: {fuel} Litrów | okrążenia: {laps}".format(
            author=ctx.author.id, fuel=math.ceil(fuel), laps=math.ceil(nof_laps)
        )
    )
    await ctx.send(content=response, mention_author=True)


bot.run(TOKEN)
