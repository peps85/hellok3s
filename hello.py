import time
from pymongo import MongoClient

# Connessione a MongoDB
client = MongoClient("mongodb://mongo:27017/")
db = client["metrics"]
collection = db["hello_world"]

i = 0
while True:
    metric = {"message": f"Hello World {i}", "timestamp": time.time()}
    collection.insert_one(metric)  # Scrive la metrica in MongoDB
    print(f"Inserted: {metric}", flush=True)
    time.sleep(1)
    i += 1
