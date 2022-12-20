import pymongo
from pprint import pprint

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["mflix"]
my_collection = db["movies_initial"]

stage_group_year = {
   "$group": {
         "_id": "$year",
         # Count the number of movies in the group:
         "movie_count": { "$sum": 1 }, 
         
   }
}

# Sort by year, ascending:
stage_sort_year_ascending = {
   "$sort": { "_id": pymongo.ASCENDING }
}

pipeline = [
   stage_group_year,
   stage_sort_year_ascending
]
results = my_collection.aggregate(pipeline)

for year in results:
    pprint(year)
