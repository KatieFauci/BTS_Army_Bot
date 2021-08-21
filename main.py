import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$pour-some-suga-on-me'):
      await message.channel.send('Show a sexy picture of suga')

    if message.content.startswith('$lets-get-handsy'):
      await message.channel.send('Show a picture of BTS hands')

    if message.content.startswith("$namtiddies"):
      await message.channel.send('show a picture of RMs chest')



    if message.content.startswith('$get-image'):
        await message.channel.send(file=discord.File('army-logo.jpg'))

client.run(os.getenv('TOKEN'))