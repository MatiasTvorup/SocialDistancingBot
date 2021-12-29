from discordBotModule import messageHandler
from discordBotModule import voiceChannelHandler
import discord

def setupBot(client):
  client = messageHandler.bindCommands(client)
  client = voiceChannelHandler.bindVoiceEvents(client)
  #Check om der er nogen inficerede personer i serveren? Hvis nej inficer en admin
  return client