from pymongo import MongoClient
from datetime import datetime
import os

client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017"))
db = client["shipping"]
collection = db["records"]

def save_shipping_record(data):
    record = {
        "itemId": data["itemId"],
        "itemName": data["itemName"],
        "quantity": data["quantity"],
        "trackingId": f"SHIP-{data['itemId'][-3:]}",
        "status": "Pending",
        "createdAt": datetime.now()
    }
    collection.insert_one(record)
    print("Saved shipping record:", record)
