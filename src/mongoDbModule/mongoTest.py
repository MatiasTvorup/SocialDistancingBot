from pymongo import MongoClient
import pymongo

CONNECTION_STRING = "mongodb://127.0.0.1:27017/"

def test():
  client = MongoClient(CONNECTION_STRING)
  db = client['testdatabase']
  # print(db)
  collection = db['test_collection']
  collection.insert_one({"name": "test", "param2": 456})
  # print(collection)


if(__name__ == "__main__"):
  test()