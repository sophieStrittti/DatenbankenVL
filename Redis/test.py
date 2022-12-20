import redis

r = redis.Redis()

r.set("test",1)
print(r.get("test"))