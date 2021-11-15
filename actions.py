import billboard
from MaxEmbeds import EmbedBuilder
import discord
import os


#------------------------------------------------
# get a channel ID
#------------------------------------------------
def get_channel_id(channel_name, client):
  channel = discord.utils.get(client.get_all_channels(), name=channel_name)
  return channel.id


#------------------------------------------------
# build display string for commands
#------------------------------------------------
def commands_string(commands):
  output = '--------------------------\n'
  for com in commands:
    output = output + f'-  {com}\t\n'

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
# checks every billboard chart for BTS
# input: Title, Description, Color, Fields, Footer, thumbnail
#------------------------------------------------
def build_embed(ti, desc, col, f_title, f_mes, foot, tn):
  embed = EmbedBuilder (
    title = ti, 
    description = desc,
    color = col,
    fields = [[f_title, f_mes, True]],
    footer = foot,
    thumbnail = tn
  ).build()
  return embed


def get_file(path):
  try:
    # try finding file as .jpg
    return discord.File(f'{path}.jpg')
  except:
    #try finding file as .gif
    try:
      print(f'GET FILE AT >>> {path}.gif')
      return discord.File(f'{path}.gif')
    except:
      print("ERROR: FILE NOT FOUND")



def get_range(dir):
  orig_dir = os.getcwd()
  os.chdir(dir)
  count = 0
  for file in enumerate(os.listdir()):
    count += 1
  os.chdir(orig_dir)
  return count-1