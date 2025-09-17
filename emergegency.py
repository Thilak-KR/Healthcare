from database import connect_db, get_collection

db = connect_db()
emergency_collection = get_collection(db, "emergencies")

def add_emergency(message, location):
    emergency_collection.insert_one({
        "message": message,
        "location": location
    })

def list_emergencies():
    return list(emergency_collection.find({}, {"_id": 0}))
