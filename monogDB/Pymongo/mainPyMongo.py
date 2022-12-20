# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pymongo
import time

if __name__ == '__main__':
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = myclient["myMonsterDatabase"]
    mycol = mydb["citibike"]

    # Experiment 1:
    myquery = {"tripduration": {"$gt": 3000000}}

    t = time.perf_counter()
    mydoc = mycol.find(myquery)

    for x in mydoc:
        print(x['bikeid'])


    print(f"Time expired for experiment 1: {time.perf_counter() - t} sec")


    # Experiment 2: jetzt erst alles in Python lesen, dann hier die
    # passenden Datensätze finden

    t = time.perf_counter()
    for x in mycol.find():
        if x["tripduration"] > 1000000:
            print(f"found element {x['bikeid']}")

    print(f"Time expired for experiment 2: {time.perf_counter() - t} sec")

    # Experiment 3: kann man es mit Hilfe von einzelnen find_one-Aufrufen erledigen?
    # Antwort: Nein;-)
    # in anderen Programmiersprachen gibt es oft ein "next()"

    # mydict = {"name": "John", "address": "Highway 37"}

    # x = mycol.insert_one(mydict)
    """
    mylist = []
    for i in range(7):
        mylist.append({ "x": i, "y": i*i})

    #print(mylist)
    x = mycol.insert_many(mylist)
    #print(x.inserted_ids)
    dblist = myclient.list_database_names()
    print(dblist)
    if "myMonsterDatabase" in dblist:
        print("The database mydatabase exists.")

    myquery = {"tripduration": {"$gt": 3000000 }}

    mydoc = mycol.find(myquery)

    for x in mydoc:
        print(x)
    """

