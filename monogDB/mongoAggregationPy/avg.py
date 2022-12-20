import pymongo
from pprint import pprint

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["mflix"]
my_collection = db["movies_initial"]

stage_group_type = {
   "$group": {
         "_id": "$type",
         # Count the number of movies in the group:
         "avg": { "$avg": "$imdbVotes" }, 
   }
}

pipeline = [
   stage_group_type,
]

results = my_collection.aggregate(pipeline)

for type in results:
    pprint(type)
