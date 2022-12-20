import pymongo
import csv
import pandas

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["imdbws_datasets"]
my_collection = db["name_basics"]

tsvFile = 'C:\\Users\\sosos\\OneDrive\\Documents\\DHBW\\Semester 5\\Datenbanken\\dataset_ imdbws\\name_basics.tsv'

csv_table = pandas.read_table(tsvFile,sep='\t')
csv_table.to_csv('name_basics.csv', index=False)

"""with open('new.csv','r', encoding="utf-8") as f:
reader = csv.DictReader(f)

new_data=[]
for each in reader:
    new_data.append(each)
    
my_collection.insert_many(new_data) 
"""

