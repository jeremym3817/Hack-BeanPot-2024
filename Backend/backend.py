# Install Flask: If you haven't already, you'll need to install Flask. You can do this using pip, the Python package manager, with the command pip install Flask.

# Set Up Your Project Structure: Create a directory for your Flask project and navigate into it. Inside this directory, you'll typically have your Python scripts, templates (HTML files), and static files (CSS, JavaScript, images).

# Write Your Flask Application Code: Create a Python script for your Flask application. This script will import Flask and define your routes, views, and any other necessary functionality.

# Define Routes: Define the URL routes for your application. These routes will map URLs to specific functions in your Flask application.

# Create Views: Write the Python functions that will handle requests to your defined routes. These functions will typically return HTML templates or JSON responses.

# Run the Development Server: Flask comes with a built-in development server that you can use to test your application locally. Run your Flask application using the command flask run in your terminal.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return {"members": ["members1","members2","members3" ]}

if __name__ == '__main__':
    app.run(debug=True)
