import pymongo
from pprint import pprint

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["mflix"]
my_collection = db["movies_initial"]

# pipeline = [
#    {
#       "$match": {
#          "title": "A Star Is Born"
#       }
#    }, 
#    {
#       "$sort": {
#          "year": pymongo.ASCENDING
#       }
#    },
# ]

# Match title = "A Star Is Born":
stage_match_title = {
   "$match": {
         "title": "A Star Is Born"
   }
}

# Sort by year, ascending:
stage_sort_year_ascending = {
   "$sort": { "year": pymongo.ASCENDING }
}

# Limit to 1 document:
stage_limit_1 = { "$limit": 1 }

# now the pipeline is easier to read
pipeline = [
   stage_match_title, 
   stage_sort_year_ascending,
   stage_limit_1,
]

results = my_collection.aggregate(pipeline)
for movie in results:
   print(" * {title}, {first_castmember}, {year}".format(
         title=movie["title"],
         first_castmember=movie["cast"],
         year=movie["year"],
   ))