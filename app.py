from flask import Flask, request, jsonify
from flask_cors import CORS
from emergency import add_emergency, list_emergencies
from medication import add_medication, list_medications
from chatbot import analyze_symptoms, save_chat

app = Flask(__name__)
CORS(app)

# Emergency routes
@app.route('/emergency', methods=['POST'])
def emergency_post():
    data = request.json
    add_emergency(data.get("message"), data.get("location"))
    return jsonify({"message": "Emergency added!"})

@app.route('/emergencies', methods=['GET'])
def emergency_get():
    return jsonify(list_emergencies())

# Medication routes
@app.route('/medication', methods=['POST'])
def medication_post():
    data = request.json
    add_medication(data.get("name"), data.get("time"))
    return jsonify({"message": "Medication added!"})

@app.route('/medications', methods=['GET'])
def medication_get():
    return jsonify(list_medications())

# Chatbot routes
@app.route('/chat', methods=['POST'])
def chat_post():
    data = request.json
    save_chat(data.get("message"))
    analysis = analyze_symptoms(data.get("message").split(","))
    return jsonify(analysis)

if __name__ == "__main__":
    app.run(debug=True)
