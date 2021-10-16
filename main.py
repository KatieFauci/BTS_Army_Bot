import discord
import os
import random
import billboard
from MaxEmbeds import EmbedBuilder
import actions

# GLOBALS
client = discord.Client()
purple = discord.Color.purple()
tag = '*'
commands = {'joon-joon', 
            'pour-some-suga-on-me',
            'WWH',
            'give-me-some-hope',
            'mr-steal-yo-girl',
            'gucci-boy',
            'give-me-a-kookie',
            'lets-get-handsy',
            'namtiddies',
            'critical-hit',
            'hot-100',
            'where-da-boys-at',
            'kill-me-with-your-thighs',
            'getting sudsy (SOPE, NOT DONE',
            'give-me-some-inspo (Quotes, NOT DONE)',
            'meme'}



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


#-------------------------------------------------------
#
#***************    IMAGE SEND COMMANDS *************** 
#
#-------------------------------------------------------


    #------------------------------------------------
    # Sends a random picture of RM
    #------------------------------------------------
    #if message.content.startswith(f'{tag}joon-joon'):
      #end = actions.get_range("images/RM")
      #print(f'RANGE >> {end}')
     # image_num = random.randint(0,actions.get_range("images/RM"))
      #image_num = random.randint(0, 50);
     # filepath = f'images/RM/{image_num}_RM'
     # print(f'FILE PATH >> {filepath}')
      #await message.channel.send(file=discord.File(filepath))
      #await message.channel.send(file=discord.File('images/RM/102_RM.jpg'))
     # await message.channel.send(file=actions.get_file(filepath))



    if message.content.startswith(f'{tag}joon-joon'):
      folder = f'RM'
      dir_path = f'images/{folder}'
      file_path = f'{dir_path}/{random.randint(0,actions.get_range(dir_path))}_{folder}'
      await message.channel.send(file=actions.get_file(file_path))


    #------------------------------------------------
    # Sends a random picture of Jin
    #------------------------------------------------


    #------------------------------------------------
    # Sends a random picture of SUGA
    #------------------------------------------------
    if message.content.startswith(f'{tag}pour-some-suga-on-me'):
      image_num = random.randint(0,581)
      filepath = f'images/Suga/{image_num}_Suga.jpg'
      await message.channel.send(file=discord.File(filepath))


    #------------------------------------------------
    # Sends a random picture of J-Hope
    #------------------------------------------------
    if message.content.startswith(f'{tag}give-me-some-hope'):
      image_num = random.randint(0,168)
      filepath = f'images/J-Hope/{image_num}_J-Hope.jpg'
      await message.channel.send(file=discord.File(filepath))


    #------------------------------------------------
    # Sends a random picture of Jimin
    #------------------------------------------------
    if message.content.startswith(f'{tag}mr-steal-yo-girl'):
      image_num = random.randint(0,144)
      filepath = f'images/Jimin/{image_num}_Jimin.jpg'
      await message.channel.send(file=discord.File(filepath))


    #------------------------------------------------
    # Sends a random picture of V
    #------------------------------------------------
    if message.content.startswith(f'{tag}gucci-boy'):
      image_num = random.randint(0,75)
      filepath = f'images/V/{image_num}_V.jpg'
      await message.channel.send(file=discord.File(filepath))


    #------------------------------------------------
    # Shows a ramdom of picture of Jungkook
    #------------------------------------------------
    if message.content.startswith(f'{tag}give-me-a-kookie'):
      image_num = random.randint(0,272)
      filepath = f'images/JK/{image_num}_JK.jpg'
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
    # Shows a random attack photo
    #------------------------------------------------
    if message.content.startswith(f'{tag}critical-hit'):
      image_num = random.randint(0,105)
      filepath = f'images/Attack/{image_num}_Attack.jpg'
      await message.channel.send(file=discord.File(filepath))

    #------------------------------------------------
    # Shows a random thirst photo of their thighs
    #------------------------------------------------
    if message.content.startswith(f'{tag}kill-me-with-your-thighs'):
      image_num = random.randint(0,37)
      filepath = f'images/Booty/{image_num}_Booty.jpg'
      await message.channel.send(file=discord.File(filepath))

    #------------------------------------------------
    # Shows a random meme
    #------------------------------------------------
    if message.content.startswith(f'{tag}meme'):
      image_num = random.randint(0,37)
      filepath = f'images/meme/{image_num}_meme.jpg'
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








    # test file extension detect
    if message.content.startswith(f'{tag}test'):
      image_num = random.randint(0,3)
      filepath = f'images/file_type_test/{image_num}_test.'
      #await message.channel.send(file=discord.File("images/file_type_test/0_test..jpg"))
      await message.channel.send(file=actions.get_file(filepath))








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