import discordBotModule
from mongoDbModule import mongoHandler

def bindVoiceEvents(client):
  @client.event
  async def on_voice_state_update(member, before, after):
    #Check at det er på channel join.
    if(after.channel != None):
      #Hent liste af alle brugere i kanalen.
      memberIds = memberListToIdList(after.channel.members)
      #Check om nogen af dem er inficeret. #Åh nej, det er jo database ting.
      memberObjectList = mongoHandler.getUserList(member.guild.id, memberIds)
      if(not channelContainsInfectedUsers(memberObjectList)):
        return
      #Get an infected user
      
      uninfectedUserIds = getUninfectedUserIds(memberObjectList)
      


      #Hvis der er en inficeret bruger: inficér alle ikke-inficerede brugere.
      print("etwas")

  
  return client

def memberListToIdList(members):
  list = []
  for member in members:
    list.append(member.id)
  return list

def channelContainsInfectedUsers(memberList):
  for member in memberList:
    if member["Infected"] == True:
      return True
  return False

def getUninfectedUserIds(memberList):
  list = []
  for member in memberList:
    if(member["Infected"==False]):
      list.append(member["UserID"])
  return list

# def infectMultipleIds(discordServerId, infectedUserIds, infectedByUserId):
#   for id in IDList:
#     mongoHandler.infectUser()