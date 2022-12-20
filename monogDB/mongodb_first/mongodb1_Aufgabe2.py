import pymongo
import csv
import pandas
import datetime

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["group_membership"]
my_collection = db["band_data"]


"""
-> convert tsv to csv
tsvFile = 'group_membership.tsv'
csv_table.pandas.read_table(tsvFile,sep='\t')
csv_table.to_csv('new.csv', index=False)
"""

"""
-> write csv to mongoDB
header = ["name","id","member","group","role","start","end"]
with open('new.csv','r', encoding="utf-8") as f:
    reader = csv.DictReader(f)

    new_data=[]
    for each in reader:
        new_data.append(each)
        
    start = datetime.datetime.now()
    my_collection.insert_many(new_data) 
    end = datetime.datetime.now()
    diff = (end - start).total_seconds()
    print(diff)
"""



