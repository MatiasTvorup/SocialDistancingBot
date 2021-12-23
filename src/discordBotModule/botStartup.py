from discordBotModule import messageHandler
import discord

def setupBot(client):
  client = messageHandler.bindCommands(client)

  return client