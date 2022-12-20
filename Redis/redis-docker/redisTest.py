import test
import datetime 
import numpy as np

client = test.Redis(host='127.0.0.1', port=6379)

for n in [1, 10, 100, 1000, 10000]:
    time = 0
    for i in range(n):
        key = f"{i}"
        value = "some value"
        start = datetime.datetime.now()
        client.get(key)
        end = datetime.datetime.now()
        diff = (end - start).total_seconds()
        time = time + diff
    
    print(n)
    print(time)