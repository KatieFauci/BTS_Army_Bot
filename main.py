import discord
import os
import random
import billboard
from MaxEmbeds import EmbedBuilder

client = discord.Client()

commands = {'pour-some-suga-on-me',
            'lets-get-handsy',
            'namtiddies',
            'hot-100',
            'where-da-boys-at (Not Done)',
            'give-me-a-kookie (Not Done)'}

#------------------------------------------------
# build display string for commands
#------------------------------------------------
def commands_string():
  output = ''
  for com in commands:
    output = output + f'-  {com}\n'

  return output

#------------------------------------------------
# Get a string containint the billboard top 10
#------------------------------------------------
def make_top_ten_string(chart):
  output = ""
  for num in range(10):
    output = output + f'{num+1} - {chart[num]}\n'

  return output


#------------------------------------------------
# checks every billboard chart for BTS
#------------------------------------------------
def find_bts_on_charts():
  charts_list = billboard.charts()
  output = []
  this_set = ''
  # check each chart
  for chart in charts_list:
    this_chart = billboard.ChartData(chart)
    rank = 0
    print(this_chart.title)
    for entry in this_chart:
      #print(str(entry))
      rank = rank + 1
      if 'BTS' in str(entry):
        this_set = this_set + f'{this_chart.title} - {rank} - {entry}\n'
        # store the current set and reset if length too long
        if len(this_set) > 900:
          print('\n RESET STRING \n')
          output.append(this_set)
          this_set = ''

  return output


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
    if message.content.startswith("<3*dobda"):
      mes = commands_string()
      print(mes)
      embed = EmbedBuilder (
        title = 'Army Commands', 
        description = 'All commands start with <3*',
        color = discord.Color.purple(),
        fields = [["List of commands:", mes, True]],
        footer = '',
        thumbnail =''
      ).build()
      await message.channel.send(embed=embed)

    #------------------------------------------------
    # Sends a random picture of SUGA
    #------------------------------------------------
    if message.content.startswith('<3*pour-some-suga-on-me'):
      image_num = random.randint(0,243)
      filepath = f'images/suga/{image_num}_suga.jpg'
      await message.channel.send(file=discord.File(filepath))


    #------------------------------------------------
    # Shows a random picture of their hands
    #------------------------------------------------
    if message.content.startswith('<3*lets-get-handsy'):
      image_num = random.randint(0,34)
      filepath = f'images/hands/{image_num}_hands.jpg'
      await message.channel.send(file=discord.File(filepath))


    #------------------------------------------------
    # Shows a random picture of RM's chest
    #------------------------------------------------
    if message.content.startswith("<3*namtiddies"):
      image_num = random.randint(0,20)
      filepath = f'images/namtiddies/{image_num}_namtiddies.jpg'
      await message.channel.send(file=discord.File(filepath))

    #------------------------------------------------
    # Shows a ramdom of picture of Jungkook
    #------------------------------------------------
    if message.content.startswith("<3*give-me-a-kookie"):
      image_num = random.randint(0,0)
      filepath = f'images/jk/{image_num}_jk.jpg'
      await message.channel.send(file=discord.File(filepath))


    #------------------------------------------------
    # Display the top ten on the hot 100
    #------------------------------------------------
    if message.content.startswith("<3*hot-100"):
      chart = billboard.ChartData('hot-100')       
      mes = make_top_ten_string(chart)
      embed = EmbedBuilder (
        title = chart.title, 
        description = '',
        color = discord.Color.purple(),
        fields = [["Top 10", mes, True]],
        footer = '',
        thumbnail =''
      ).build()
      await message.channel.send(embed=embed)


    #------------------------------------------------
    # Showes every place that bts is currently charting on billbord
    #------------------------------------------------
    if message.content.startswith("<3*where-da-boys-at"):
      await message.channel.send("checking all Billboard Charts, This may take a minute...")
      mes = find_bts_on_charts()
      count = 1
      for this_mes in mes:
        embed = EmbedBuilder (
          title = f'BTS Chart Placement Pt. {count}', 
          description = '',
          color = discord.Color.purple(),
          fields = [["Where they are Charting:", this_mes, True]],
          footer = '',
          thumbnail =''
        ).build()
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