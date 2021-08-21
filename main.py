import discord
import os
import random

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('<3*hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('<3*pour-some-suga-on-me'):
      image_num = random.randint(0,199)
      filepath = f'images/suga/{image_num}_suga.jpg'
      await message.channel.send(file=discord.File(filepath))

    if message.content.startswith('<3*lets-get-handsy'):
      image_num = random.randint(0,199)
      filepath = f'images/suga/{image_num}_hands.jpg'
      await message.channel.send(file=discord.File(filepath))

    if message.content.startswith("<3*namtiddies"):
      await message.channel.send('show a picture of RMs chest')


client.run(os.getenv('TOKEN'))