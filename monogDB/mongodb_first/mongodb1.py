import pymongo
from pprint import pprint

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["med_data"]
my_collection = db["patient_data"]

patient_records = [
 {
   "Name": "Adam Blythe",
   "Age": 55,
   "Sex": "M",
   "Blood pressure": [{"sys": 132}, {"dia": 73}],
   "Heart rate": 73
 },
 {
   "Name": "Darren Sanders",
   "Age": 34,
   "Sex": "M",
   "Blood pressure": [{"sys": 120}, {"dia": 70}],
   "Heart rate": 67
 },
 {
   "Name": "Sally-Ann Joyce",
   "Age": 19,
   "Sex": "F",
   "Blood pressure": [{"sys": 121}, {"dia": 72}],
   "Heart rate": 67
 }
]
my_collection.insert_many(patient_records)
for item in my_collection.find():
    pprint(item)
