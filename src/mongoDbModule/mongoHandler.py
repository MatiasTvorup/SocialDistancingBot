from pymongo import MongoClient
import pymongo
import time

CONNECTION_STRING = "mongodb://127.0.0.1:27017/"

def __getCollection(discordServerId):
  client = MongoClient(CONNECTION_STRING)
  db = client['SocialDistancieringsBotDB']
  collection = db[str(discordServerId)]
  return collection


def insertNewUser(discordServerId, userId):
  #User dataformat
  #{"UserID": 123, "Infected": false, "InfectedbyUserID":456, "InfectedAtTimestamp":123654789}
  col = __getCollection(discordServerId)
  return col.insert_one({"UserID":userId, "Infected":False, "InfectedByUserId":None, "InfectedAtTimestamp":0}).inserted_id

def infectUser(discordServerId, infectedUserId, infectedByUserId):
  col = __getCollection(discordServerId)
  #CHeck om bruger findes i collection
  if(not col.find({"UserID":infectedUserId}).alive):
    #Indsæt hvis den ikke gør.
    insertNewUser(discordServerId, infectedUserId)
  #Derefter opdater
  member = col.find_one({"UserID":infectedUserId})
  if(member["Infected"] == True):
    return
  col.update_one({"UserID":infectedUserId},{"$set":{"Infected":True, "InfectedByUserId":infectedByUserId, "InfectedAtTimestamp":time.time()}})

def getUserList(discordServerId, userIdList):
  col = __getCollection(discordServerId)
  listOfUserDicts = []
  cursor = col.find({"UserID":{"$in":userIdList}})
  for user in cursor:
    listOfUserDicts.append(user)
  return listOfUserDicts

def getUserIdList(discordServerId):
  col = __getCollection(discordServerId)
  cursor = list(col.find({},{"UserID":1, "_id":0}))
  l = []
  for c in cursor:
    l.append(c["UserID"])
  return l


def getSingleUser(discordServerId, userId):
  col = __getCollection(discordServerId)
  user = col.find_one({"UserID": userId})
  if(user == None):
    insertNewUser(discordServerId, userId)
    return getSingleUser(discordServerId, userId)
  else:
    return user


if __name__ == "__main__":
  insertNewUser("ServerID", "Dillarmanden")
  print(getSingleUser("ServerID", "Dillarmanden"))