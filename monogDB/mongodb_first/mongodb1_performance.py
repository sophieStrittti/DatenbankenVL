import pymongo
from pprint import pprint
import datetime
import numpy as np
import json

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["performanceVSRedis"]
my_collection = db["performanceTest"]

for n in [10, 100, 1000, 10000]:
    new_data = []

    for i in range(n):
        data = '{"' + str(i) + '": "some value"}'
        data = json.loads(data) 
        new_data.append(data)
        
    start = datetime.datetime.now()
    my_collection.find({})
    end = datetime.datetime.now()
    diff = (end - start).total_seconds()
    print(n)
    print(diff)


    






