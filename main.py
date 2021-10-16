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
image_com = ['joon-joon', 
            'WWH',
            'pour-some-suga-on-me',
            'give-me-some-hope',
            'mr-steal-yo-girl',
            'gucci-boy',
            'give-me-a-kookie',
            'lets-get-handsy',
            'namtiddies',
            'critical-hit',
            'kill-me-with-your-thighs',]

act_com = ['hot-100',
          'where-da-boys-at',]



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
      image_commands = actions.commands_string(image_com)
      action_commands = actions.commanfs_string(act_com)
      embed = actions.build_embed('Army Commands', '', purple, "Get Random Image:", image_commands, 'Actions:', action_commands)
      await message.channel.send(embed=embed)


#-------------------------------------------------------
#
#***************    IMAGE SEND COMMANDS *************** 
#
#-------------------------------------------------------


    #------------------------------------------------
    # Sends a random picture of RM
    #------------------------------------------------
    if message.content.startswith(f'{tag}{image_com[0]}'):
      folder = f'RM'
      dir_path = f'images/{folder}'
      file_path = f'{dir_path}/{random.randint(0,actions.get_range(dir_path))}_{folder}'
      await message.channel.send(file=actions.get_file(file_path))


    #------------------------------------------------
    # Sends a random picture of Jin
    #------------------------------------------------
    if message.content.startswith(f'{tag}{image_com[1]}'):
      folder = f'Jin'
      dir_path = f'images/{folder}'
      file_path = f'{dir_path}/{random.randint(0,actions.get_range(dir_path))}_{folder}'
      await message.channel.send(file=actions.get_file(file_path))


    #------------------------------------------------
    # Sends a random picture of SUGA
    #------------------------------------------------
    if message.content.startswith(f'{tag}{image_com[2]}'):
      folder = f'SUGA'
      dir_path = f'images/{folder}'
      file_path = f'{dir_path}/{random.randint(0,actions.get_range(dir_path))}_{folder}'
      await message.channel.send(file=actions.get_file(file_path))


    #------------------------------------------------
    # Sends a random picture of J-Hope
    #------------------------------------------------
    if message.content.startswith(f'{tag}{image_com[3]}'):
      folder = f'J-Hope'
      dir_path = f'images/{folder}'
      file_path = f'{dir_path}/{random.randint(0,actions.get_range(dir_path))}_{folder}'
      await message.channel.send(file=actions.get_file(file_path))


    #------------------------------------------------
    # Sends a random picture of Jimin
    #------------------------------------------------
    if message.content.startswith(f'{tag}{image_com[4]}'):
      folder = f'Jimin'
      dir_path = f'images/{folder}'
      file_path = f'{dir_path}/{random.randint(0,actions.get_range(dir_path))}_{folder}'
      await message.channel.send(file=actions.get_file(file_path))


    #------------------------------------------------
    # Sends a random picture of V
    #------------------------------------------------
    if message.content.startswith(f'{tag}{image_com[5]}'):
      folder = f'V'
      dir_path = f'images/{folder}'
      file_path = f'{dir_path}/{random.randint(0,actions.get_range(dir_path))}_{folder}'
      await message.channel.send(file=actions.get_file(file_path))


    #------------------------------------------------
    # Shows a ramdom of picture of Jungkook
    #------------------------------------------------
    if message.content.startswith(f'{tag}{image_com[6]}'):
      folder = f'JK'
      dir_path = f'images/{folder}'
      file_path = f'{dir_path}/{random.randint(0,actions.get_range(dir_path))}_{folder}'
      await message.channel.send(file=actions.get_file(file_path))



    #------------------------------------------------
    # Shows a random picture of their hands
    #------------------------------------------------
    if message.content.startswith(f'{tag}{image_com[7]}'):
      folder = f'hands'
      dir_path = f'images/{folder}'
      file_path = f'{dir_path}/{random.randint(0,actions.get_range(dir_path))}_{folder}'
      await message.channel.send(file=actions.get_file(file_path))



    #------------------------------------------------
    # Shows a random picture of RM's chest
    #------------------------------------------------
    if message.content.startswith(f'{tag}{image_com[8]}'):
      folder = f'namtiddies'
      dir_path = f'images/{folder}'
      file_path = f'{dir_path}/{random.randint(0,actions.get_range(dir_path))}_{folder}'
      await message.channel.send(file=actions.get_file(file_path))



    #------------------------------------------------
    # Shows a random attack photo
    #------------------------------------------------
    if message.content.startswith(f'{tag}{image_com[9]}'):
      folder = f'Attack'
      dir_path = f'images/{folder}'
      file_path = f'{dir_path}/{random.randint(0,actions.get_range(dir_path))}_{folder}'
      await message.channel.send(file=actions.get_file(file_path))

    #------------------------------------------------
    # Shows a random thirst photo of their thighs
    #------------------------------------------------
    if message.content.startswith(f'{tag}{image_com[10]}'):
      folder = f'Booty'
      dir_path = f'images/{folder}'
      file_path = f'{dir_path}/{random.randint(0,actions.get_range(dir_path))}_{folder}'
      await message.channel.send(file=actions.get_file(file_path))

    #------------------------------------------------
    # Shows a random meme
    #------------------------------------------------
    if message.content.startswith(f'{tag}{image_com[11]}'):
      folder = f'meme'
      dir_path = f'images/{folder}'
      file_path = f'{dir_path}/{random.randint(0,actions.get_range(dir_path))}_{folder}'
      await message.channel.send(file=actions.get_file(file_path))





#-------------------------------------------------------
#
#***************    ACTION COMMANDS   ****************** 
#
#-------------------------------------------------------



    #------------------------------------------------
    # Display the top ten on the hot 100
    #------------------------------------------------
    if message.content.startswith(f'{tag}{act_com[0]}'):
      chart = billboard.ChartData('hot-100')       
      mes = actions.make_top_ten_string(chart)
      embed = actions.build_embed(chart.title, '', purple, "Top 10", mes, '', '')
      await message.channel.send(embed=embed)


    #------------------------------------------------
    # Showes every place that bts is currently charting on billbord
    #------------------------------------------------
    if message.content.startswith(f'{tag}{act_com[1]}'):
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