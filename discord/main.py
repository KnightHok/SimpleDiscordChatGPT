import discord
from discord import app_commands
from discord.ext import commands
import openai
import os
from dotenv import load_dotenv
from time import sleep

# import prompts
from prompts import chatgpt

load_dotenv("../.env")
print(os.getenv("OPENAI_API_KEY"))

openai.api_key = os.getenv("OPENAI_API_KEY")


intents = discord.Intents.default()
intents.message_content = True

# client = discord.Client(intents=intents)

bot = commands.Bot(intents=intents, command_prefix='$')

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return

#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')


@bot.tree.command(
    name="hello",
    description="this is a mad level description"
)
async def hello_command(interaction: discord.Interaction):
    print("helloing :)")
    await interaction.response.send_message("we made it")

@bot.tree.command(
    name="hello2",
    description="this is another description"
)
async def hellos_command(interaction: discord.Interaction):
    print("helloing :)")
    await interaction.response.send_message("we made it")


@bot.tree.command(
    name="chatgpt_rand_fruit",
    description="ask chatgpt about a random fruit"
)
async def chatgpt_fruit(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=True)
    response = await chatgpt()
    # bot.wait_for("message", check=response)
    # print(response.choices[0].text)
    # print(len(response.choices[0].text))
    # await interaction.response.send_message(response.choices[0].text)
    await interaction.followup.send(response.choices[0].text)

@bot.tree.command(
    name="chatgpt_ask",
    description="ask chatgpt a question"
)
async def chatgpt_ask(interaction: discord.Interaction, question: str):
    await interaction.response.defer(ephemeral=True)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        temperature=0.6,
        max_tokens=100
    )
    await interaction.followup.send(response.choices[0].text)

@bot.command(name="sync_bot", description="some small description")
async def sync_command(ctx):
    await bot.tree.sync()
    print("synced up :)")
    await ctx.send("damn")

bot.run(os.getevn("DISCORD_KEY"))