from pymongo import MongoClient
import pymongo

CONNECTION_STRING = "mongodb://127.0.0.1:27017/"

def test():
  client = MongoClient(CONNECTION_STRING)
  db = client['testdatabase']
  # print(db)
  collection = db['test_collection']
  # collection.insert_one({"name": "test", "param2": 456})
  # collection.insert_one({"name": "test", "param2": 752})
  # collection.insert_one({"name": "test", "param2": 123})
  # collection.insert_one({"name": "test", "param2": 785})
  # collection.insert_one({"name": "test", "param2": 643})
  # collection.insert_one({"name": "test", "param2": 789})
  # out = collection.find_one({"name":"test2"})
  out = collection.find({"name": "test"})
  for e in out:
    print(e)
  # print(out)

  # print(collection)


if(__name__ == "__main__"):
  test()