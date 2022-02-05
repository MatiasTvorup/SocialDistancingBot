from discordBotModule import messageHandler
from discordBotModule import voiceChannelHandler
from discordBotModule import userHandler
import discord

def setupBot(client):
  intents = discord.Intents.all()
  client = discord.Client(intents=intents)

  client = messageHandler.bindCommands(client)
  client = voiceChannelHandler.bindVoiceEvents(client)
  client = userHandler.bindUserEvents(client)
  #Check om der er nogen inficerede personer i serveren? Hvis nej inficer en admin
  return client
