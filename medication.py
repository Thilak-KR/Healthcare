from database import connect_db, get_collection
from datetime import datetime

db = connect_db()
medication_collection = get_collection(db, "medications")

def add_medication(name, time):
    medication_collection.insert_one({
        "name": name,
        "time": time
    })

def list_medications():
    return list(medication_collection.find({}, {"_id":0}))
