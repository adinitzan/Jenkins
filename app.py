from flask import Flask

# Create a Flask app
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
