
from flask import Flask, request, jsonify
from pymongo.mongo_client import MongoClient
from pprint import pprint

uri = "mongodb+srv://dcleader99:ztjVWZHUmqTrZMi5@hackbeanpot.lrlzr0q.mongodb.net/?retryWrites=true&w=majority&appName=Hackbeanpot"

# Create a new client and connect to the server
client = MongoClient(uri)
# Connect to MongoDB Atlas
# Replace <username>, <password>, <cluster_name>, and <database_name> with your own values
db = client.get_database('classes')  # Replace <database_name> with your own database name
collection = db['neu']  # Replace 'your_collection' with your own collection name

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    pprint(collection)
except Exception as e:
    print(e)

from flask import Flask, request, jsonify

app = Flask(__name__)