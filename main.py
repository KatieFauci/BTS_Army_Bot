import discord
import os
import random
import billboard
from MaxEmbeds import EmbedBuilder
import actions

# GLOBALS
client = discord.Client()
purple = discord.Color.purple()
tag = '<3*'
commands = {'pour-some-suga-on-me',
            'give-me-a-kookie (NOT DONE)',
            'mr-steal-yo-girl (NOT DONE)',
            'WWH (NOT DONE)',
            'lets-get-handsy',
            'namtiddies',
            'hot-100',
            'where-da-boys-at',
            'kill-me-with-your-thighs (NOT DONE)',
            'getting sudsy (SOPE, NOT DONE',
            'give-me-some-inspo (NOT DONE)'}



#------------------------------------------------
# Log On message
#------------------------------------------------
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


#------------------------------------------------
# ON MESSAGE
#------------------------------------------------
@client.event
async def on_message(message):
  if not message.author.bot:
    if message.author == client.user:
        return

    #------------------------------------------------
    # Lists All commands
    #------------------------------------------------
    if message.content.startswith(f'{tag}help'):
      mes = actions.commands_string(commands)
      print(mes)
      embed = actions.build_embed('Army Commands', '', purple, "Commands:", mes, '', '')
      await message.channel.send(embed=embed)

    #------------------------------------------------
    # Sends a random picture of RM
    #------------------------------------------------
    if message.content.startswith(f'{tag}Joon-Joon'):
      image_num = random.randint(0,243)
      filepath = f'images/suga/{image_num}_suga.jpg'
      await message.channel.send(file=discord.File(filepath))


    #------------------------------------------------
    # Sends a random picture of SUGA
    #------------------------------------------------
    if message.content.startswith(f'{tag}pour-some-suga-on-me'):
      image_num = random.randint(0,243)
      filepath = f'images/suga/{image_num}_suga.jpg'
      await message.channel.send(file=discord.File(filepath))


    #------------------------------------------------
    # Shows a random picture of their hands
    #------------------------------------------------
    if message.content.startswith(f'{tag}lets-get-handsy'):
      image_num = random.randint(0,34)
      filepath = f'images/hands/{image_num}_hands.jpg'
      await message.channel.send(file=discord.File(filepath))


    #------------------------------------------------
    # Shows a random picture of RM's chest
    #------------------------------------------------
    if message.content.startswith(f'{tag}namtiddies'):
      image_num = random.randint(0,20)
      filepath = f'images/namtiddies/{image_num}_namtiddies.jpg'
      await message.channel.send(file=discord.File(filepath))

    #------------------------------------------------
    # Shows a ramdom of picture of Jungkook
    #------------------------------------------------
    if message.content.startswith(f'{tag}give-me-a-kookie'):
      image_num = random.randint(0,0)
      filepath = f'images/jk/{image_num}_jk.jpg'
      await message.channel.send(file=discord.File(filepath))


    #------------------------------------------------
    # Display the top ten on the hot 100
    #------------------------------------------------
    if message.content.startswith(f'{tag}hot-100'):
      chart = billboard.ChartData('hot-100')       
      mes = actions.make_top_ten_string(chart)
      embed = actions.build_embed(chart.title, '', purple, "Top 10", mes, '', '')
      await message.channel.send(embed=embed)


    #------------------------------------------------
    # Showes every place that bts is currently charting on billbord
    #------------------------------------------------
    if message.content.startswith(f'{tag}where-da-boys-at'):
      await message.channel.send("checking all Billboard Charts, This may take a minute...")
      mes = actions.find_bts_on_charts()
      count = 1
      for this_mes in mes:
        embed = actions.build_embed(f'BTS Chart Placement Pt. {count}', '', purple, "Where they are Charting:", this_mes, '', '')
        await message.channel.send(embed=embed)
        count = count + 1









    if message.content.startswith("<3*embed-test"):
      mes = ''
      # make a test string
      for num in range(1024):
        mes = mes + 'o'

      print(f'STRING LENGTH: {len(mes)}')
      embed = EmbedBuilder (
        title = "MaxEmbeds - EmbedBuilder", 
        description = "Test description",
        color = discord.Color.dark_gold(),
        fields = [["Test", mes, True]],
        footer = ["Test footer", message.author.avatar_url],
        thumbnail = message.author.avatar_url
      ).build()

      await message.channel.send(embed=embed)




client.run(os.getenv('TOKEN'))