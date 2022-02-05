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
      memberObjectList = mongoHandler.getUserList(str(member.guild.id), memberIds)

      infectedMember = getInfectedUser(memberObjectList)
      if(infectedMember == None):
        return

      #Get an infected user
      uninfectedUserIds = getUninfectedUserIds(memberObjectList)
      
      #Infect andre brugere i voice kanalen.
      for userId in uninfectedUserIds:
        mongoHandler.infectUser(member.guild.id,userId, infectedMember["UserID"])

  return client

def memberListToIdList(members):
  list = []
  for member in members:
    list.append(str(member.id))
  return list

def getInfectedUser(memberList):
  for member in memberList:
    if member["Infected"] == True:
      return member
  return None

def getUninfectedUserIds(memberList):
  list = []
  for member in memberList:
    if(member["Infected"] == False):
      list.append(member["UserID"])
  return list

# def infectMultipleIds(discordServerId, infectedUserIds, infectedByUserId):
#   for id in IDList:
#     mongoHandler.infectUser()