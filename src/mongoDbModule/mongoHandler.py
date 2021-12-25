from pymongo import MongoClient
import pymongo
import time

CONNECTION_STRING = "mongodb://127.0.0.1:27017/"

def __getCollection(discordServerId):
  client = MongoClient(CONNECTION_STRING)
  db = client['SocialDistancieringsBotDB']
  collection = db[discordServerId]
  return collection


def insertNewUser(discordServerId, userId):
  #User dataformat
  #{"UserID": 123, "Infected": false, "InfectedbyUserID":456, "InfectedAtTimestamp"}
  col = __getCollection(discordServerId)
  return col.insert_one({"UserID":userId, "Infected":False, "InfectedByUserId":None, "InfectedAtTimestamp":0}).inserted_id

def infectUser(discordServerId, infectedUserId, infectedByUserId):
  col = __getCollection(discordServerId)
  #CHeck om bruger findes i collection
  if(col.find({"UserID":infectedUserId}).count() > 0):
    #Indsæt hvis den ikke gør.
    insertNewUser(discordServerId, infectedUserId)
  #Derefter opdater
  col.update_one({"UserID":infectedUserId},{"$set":{"Infected":True, "InfectedByUserId":infectedByUserId, "InfectedAtTimestamp":time.time()}})

if __name__ == "__main__":
  x = insertNewUser("serverID"," mongobongo")
  print(x)
  col = __getCollection("serverID")
  y = col.find_one({"_id":x})
  print(y)