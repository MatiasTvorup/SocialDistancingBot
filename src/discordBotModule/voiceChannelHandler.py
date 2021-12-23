import discordBotModule

def bindVoiceEvents(client):
  @client.event
  async def on_voice_state_update(member, before, after):
    #Check at det er på channel join.
    if(after.channel != None):
      #Hent liste af alle brugere i kanalen.
      memberIds = memberListToIdList(after.channel.members)
      #Check om nogen af dem er inficeret. #Åh nej, det er jo database ting.
      #Hvis der er en inficeret bruger: inficér alle ikke-inficerede brugere.
      print("etwas")

  
  return client

def memberListToIdList(members):
  list = []
  for member in members:
    list.append(member.id)
  return list