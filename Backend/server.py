# Install Flask: If you haven't already, you'll need to install Flask. You can do this using pip, the Python package manager, with the command pip install Flask.

# Set Up Your Project Structure: Create a directory for your Flask project and navigate into it. Inside this directory, you'll typically have your Python scripts, templates (HTML files), and static files (CSS, JavaScript, images).

# Write Your Flask Application Code: Create a Python script for your Flask application. This script will import Flask and define your routes, views, and any other necessary functionality.

# Define Routes: Define the URL routes for your application. These routes will map URLs to specific functions in your Flask application.

# Create Views: Write the Python functions that will handle requests to your defined routes. These functions will typically return HTML templates or JSON responses.

# Run the Development Server: Flask comes with a built-in development server that you can use to test your application locally. Run your Flask application using the command flask run in your terminal.



from flask import Flask, request, jsonify
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
from pprint import pprint
# from TestMongoQuery import queryInsert, querySearch
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
uri = os.getenv("DATABASE_URL")

# Create a new client and connect to the server
client = MongoClient(uri)
# Connect to MongoDB Atlas
# Replace <username>, <password>, <cluster_name>, and <database_name> with your own values
db = client.get_database('<database_name>')  # Replace <database_name> with your own database name
collection = db['your_collection']  # Replace 'your_collection' with your own collection name

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


app = Flask(__name__)

# @app.route('/api', methods=['POST'])
# def receive_json():
#     if request.method == 'POST': #JSON received for Querying
#         if request.is_json:
#             data = request.json  # Get JSON data from the request
#             new_id = data["id"]
#             new_course_name = data["class_name"]
#             new_timeslot = data["timeslot"]
            
#             new_obj = {
#                 '_id': new_id,
#                 "class_name": new_course_name,
#                 "timeslot": new_timeslot
#             }
#             obj_json = jsonify(new_obj)
#             queryInsert(obj_json)
#             # Process the received data (optional)
#             # For example, you can save it to a database, perform calculations, etc.

#             # Send a response back to the client
#             response = {"message": "JSON received successfully"}
#             return jsonify(response), 200
#         else:
#             return jsonify({"error": "Request must be JSON"}), 400

@app.route('/', methods=['GET'])
def receive_json():
    if request.method == 'GET': #JSON received for Querying
        cursor = collection.find({"_id":1})
        document_list = []
        for i in cursor:
            document_list.append(i)
        response = {"message": "JSON received successfully"}
        return jsonify(document_list), 200
        # Process the received data (optional)
        # For example, you can save it to a database, perform calculations, etc.

        # Send a response back to the client

        # return jsonify(response), 200
    else:
        return jsonify({"error": "Request must be JSON"}), 400

if __name__ == '__main__':
    app.run(debug=True)












# Define routes
@app.route('/api/data', methods=['GET'])
def get_data():
    data = list(collection.find({}))  # Retrieve all documents from the collection
    return jsonify(data), 200

@app.route('/api/data', methods=['POST'])
def add_data():
    new_data = request.json  # Get JSON data from the request body
    collection.insert_one(new_data)  # Insert new document into the collection
    return jsonify({"message": "Data added successfully"}), 201

# Creating the start of the route

if __name__ == '__main__':
    app.run(debug=True)
