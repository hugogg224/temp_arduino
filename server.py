import os
from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)  # permite acceder desde cualquier web

# MongoDB
mongo_uri = "mongodb+srv://hh:BYvwcNLuZ7EYwT0j@cluster0.axpsmqb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client_db = MongoClient(mongo_uri)
db = client_db.sensor
collection = db.Temperatura

@app.route("/ultimo")
def ultimo():
    doc = collection.find_one(sort=[('_id', -1)])
    return str(doc['tempC'])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # usa el puerto que da Railway
    app.run(host="0.0.0.0", port=port)
