import discord
from mongoDbModule import mongoHandler
from datetime import datetime

def bindCommands(client):
  # newclient = client
  
  @client.event
  async def on_message(message):
    #Check at beskeden ikke er fra os selv.¨
    if(message.author == client.user):
      return
    #Kommando hvis vi bliver @'et.
    elif(client.user in message.mentions):
      await message.channel.send("Type !SDB_help for a list of commands.")
    #Kommando for help
    elif(message.content == "!SDB_help"):
      await message.channel.send(helpInstructions())
    #Kommando for serverstats
    #Kommando for egne stats
    elif(message.content == "!SDB_me"):
      await message.channel.send(userStats(client, message.author.id, message.guild.id))
    #Kommando for forklaring
    elif(message.content == "!SDB_what"):
      await message.channel.send(botExplanation(client))
    # await message.channel.send("*yeet*")

  return client

def helpInstructions():
  return """
**!SDB_help** - Shows a list of commands.
**!SDB_server** - Shows percentage of 'infected' users in this server.
**!SDB_me** - Shows if you are 'infected', when you where infected and by who.
**!SDB_what** - Shows an explanation of what this bot does."""

def botExplanation(client):
  return """
  This is """ + client.user.display_name + """, a game inspired by 'Rona and the MW3 gamemode 'Infected'. At the start of the game, a person in the server is marked as 'Infected'. If an 'infected' person is in a voicecall with other people, those too become 'infected'.
  """

def userStats(client, userID, serverID):
  user = mongoHandler.getSingleUser(serverID, userID)
  if(user["Infected"]==True):
    infectedByName = client.get_user(user["InfectedbyUserID"]).display_name
    return "You have been infected by " + infectedByName + " at " + datetime.utcfromtimestamp(user["InfectedAtTimestamp"]).strftime('%Y-%m-%d %H:%M:%S')
  else:
    return "You haven't been infected.\nYet."