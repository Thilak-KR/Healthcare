from database import connect_db, get_collection

db = connect_db()
chat_collection = get_collection(db, "chats")

# Very basic symptom-disease mapping for demo
SYMPTOM_DB = {
    "fever": ["Flu", "Common Cold"],
    "cough": ["Flu", "Bronchitis"],
    "rash": ["Allergy", "Measles"],
    "headache": ["Migraine", "Stress"]
}

def analyze_symptoms(symptoms):
    result = {}
    for symptom in symptoms:
        diseases = SYMPTOM_DB.get(symptom.lower(), ["Unknown"])
        result[symptom] = diseases
    return result

def save_chat(user_input):
    chat_collection.insert_one({"message": user_input})
