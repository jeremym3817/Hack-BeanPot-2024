
from pymongo.mongo_client import MongoClient
from pprint import pprint
import json


uri = "mongodb+srv://dcleader99:ztjVWZHUmqTrZMi5@hackbeanpot.lrlzr0q.mongodb.net/?retryWrites=true&w=majority&appName=Hackbeanpot"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# db = client.test_database or db = client["test-database"]
db = client["classes"]

#Getting a collection
# collection = db.test_collection or collection = db["test-collection"]
collection = db["neu"]

# Open the JSON file in read mode
# with open('newData.json', 'r') as file:
#     json_data = json.load(file)
cursor = collection.find({"_id":1})
for i in cursor:
    pprint(i)
# def queryInsert(json_object):
#     if isinstance(json_data, list):
#         collection.insert_many(json_data)
#     else:
#         collection.insert_one(json_data)
# def querySearch():
#     if isinstance(json_data, list):
#         collection.find({})
#         # collection.find({"_id":json_data["_id"]})
#     else:
#         print("Not possible, error: Based on incorrect json.")