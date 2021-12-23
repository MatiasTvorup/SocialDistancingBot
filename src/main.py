from loadCredentialsModule import loadCredentials
from discordBotModule import botStartup
import discord

def main():
  credentials = loadCredentials.loadCredentialsFromFile("credentials.txt")
  client = discord.Client()
  client = botStartup.setupBot(client)
  client.run(credentials[0])


if __name__ == "__main__":
  main()
