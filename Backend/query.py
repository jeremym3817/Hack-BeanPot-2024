
from pymongo.mongo_client import MongoClient
import pprint

uri = "mongodb+srv://dcleader99:ztjVWZHUmqTrZMi5@hackbeanpot.lrlzr0q.mongodb.net/?retryWrites=true&w=majority&appName=Hackbeanpot"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.test_database # or db - client["test-database"]

#Getting a collection
collection = db.test_collection # or collection = db["test-collection"]


pprint.pprint(posts.find_one())