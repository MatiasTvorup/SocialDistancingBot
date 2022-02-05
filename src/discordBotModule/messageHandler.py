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
    elif(message.content.lower() == "!SDB_help".lower()):
      await message.channel.send(helpInstructions())
    #Kommando for serverstats
    #Kommando for egne stats
    elif(message.content.lower() == "!SDB_me".lower()):
      await message.channel.send(userStats(client, message.author.id, message.guild.id))
    #Kommando for forklaring
    elif(message.content.lower() == "!SDB_what".lower()):
      await message.channel.send(botExplanation(client))
    elif(message.content.lower() == "!SDB_server".lower()):
      await message.channel.send(serverStats(message.guild))
      

  return client

def helpInstructions():
  return """
**!SDB_help** - Shows a list of commands.
**!SDB_server** - Shows how many users in this server are 'infected'.
**!SDB_me** - Shows if you are 'infected', when you were infected and by who.
**!SDB_what** - Shows an explanation of what this bot does."""

def botExplanation(client):
  return """
  This is """ + client.user.display_name + """, a game inspired by 'Rona and the MW3 gamemode 'Infected'. At the start of the game, a person in the server is marked as 'Infected'. If an 'infected' person is in a voicecall with other people, those too become 'infected'.
  """

def userStats(client, userID, serverID):
  user = mongoHandler.getSingleUser(str(serverID), str(userID))
  if(user["Infected"]==True):
    infectedBy = client.get_user(int(user["InfectedByUserId"]))
    infectedByName = infectedBy.display_name if infectedBy != None else "licking a doorknob"
    return "You have been infected by " + infectedByName + " at " + datetime.utcfromtimestamp(user["InfectedAtTimestamp"]).strftime('%Y-%m-%d %H:%M:%S')
  else:
    return "You haven't been infected.\nYet."

def serverStats(guild):
  memberCount = guild.member_count
  infectedCount = len(mongoHandler.getInfectedUsers(guild.id))
  return  str(infectedCount) + " out of " + str(memberCount) + " people have been infected."