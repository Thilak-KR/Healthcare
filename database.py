from pymongo import MongoClient

def connect_db():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["healthcare_app"]
    return db

def get_collection(db, name):
    return db[name]
