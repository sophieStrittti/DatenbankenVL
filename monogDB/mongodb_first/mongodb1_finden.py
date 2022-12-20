import pymongo
from pprint import pprint

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["tif20"]
my_collection = db["radl"]

test = my_collection.find({"start_station_id": "3202.06"})
for item in test:
    pprint(item)

