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
      await message.channel.send('Show a sexy picture of suga')

    if message.content.startswith('<3*lets-get-handsy'):
      await message.channel.send('Show a picture of BTS hands')

    if message.content.startswith("<3*namtiddies"):
      await message.channel.send('show a picture of RMs chest')

    if message.content.startswith('<3*get-image'):
      image_num = random.randint(0,199)
      filepath = f'images/suga/{image_num}_suga.jpg'
      #await message.channel.send(file=discord.File('1_suga.jpg'))
      await message.channel.send(file=discord.File(filepath))
      #https://replit.com/@KatieFauci/BTSArmyBot#images/suga/1_suga.jpg

client.run(os.getenv('TOKEN'))