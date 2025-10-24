from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)  # Permitir CORS desde cualquier origen

# Conexión a MongoDB
mongo_uri = "mongodb+srv://hh:BYvwcNLuZ7EYwT0j@cluster0.axpsmqb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client_db = MongoClient(mongo_uri)
db = client_db.sensor
collection = db.Temperatura

@app.route("/ultimo")
def ultimo():
    doc = collection.find_one(sort=[('_id', -1)])
    return jsonify({"tempC": float(doc['tempC'])})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
