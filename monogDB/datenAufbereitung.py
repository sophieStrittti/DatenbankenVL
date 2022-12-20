import pymongo
from pprint import pprint
from bson.objectid import ObjectId

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["imdb_datasets"]
my_collection = db["name_basics"]

stage_group_type = {
   "$match": {
         "birthYear": ""
   }
}

pipeline = [
   stage_group_type,
]

results = my_collection.find({'birthYear': { '$exists': False}})


i = 1
for result in results:
    my_collection.delete_one(result)
    print(i)
    i = i + 1

print("done")
