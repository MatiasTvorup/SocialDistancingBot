from discordBotModule import messageHandler
from discordBotModule import voiceChannelHandler
import discord

def setupBot(client):
  client = messageHandler.bindCommands(client)
  client = voiceChannelHandler.bindVoiceEvents(client)
  return client