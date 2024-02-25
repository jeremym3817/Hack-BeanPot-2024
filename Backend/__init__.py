# Install Flask: If you haven't already, you'll need to install Flask. You can do this using pip, the Python package manager, with the command pip install Flask.

# Set Up Your Project Structure: Create a directory for your Flask project and navigate into it. Inside this directory, you'll typically have your Python scripts, templates (HTML files), and static files (CSS, JavaScript, images).

# Write Your Flask Application Code: Create a Python script for your Flask application. This script will import Flask and define your routes, views, and any other necessary functionality.

# Define Routes: Define the URL routes for your application. These routes will map URLs to specific functions in your Flask application.

# Create Views: Write the Python functions that will handle requests to your defined routes. These functions will typically return HTML templates or JSON responses.

# Run the Development Server: Flask comes with a built-in development server that you can use to test your application locally. Run your Flask application using the command flask run in your terminal.

from flask import Flask, request, jsonify
# from flask_pymongo import PyMongo
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://dcleader99:ztjVWZHUmqTrZMi5@hackbeanpot.lrlzr0q.mongodb.net/?retryWrites=true&w=majority&appName=Hackbeanpot"

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

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/receive', methods=['POST'])
def receive_json():
    if request.is_json:
        data = request.json  # Get JSON data from the request
        
        print("Received JSON:", data)
        
        # Process the received data (optional)
        # For example, you can save it to a database, perform calculations, etc.

        # Send a response back to the client
        response = {"message": "JSON received successfully"}
        return jsonify(response), 200
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
