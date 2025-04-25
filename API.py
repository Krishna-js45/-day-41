from flask import Flask, jsonify, request

# Create a Flask application instance
app = Flask(__name__)

# A simple route to return a message
@app.route('/')
def home():
    return "Welcome to my Flask API!"

# A route to return a JSON response
@app.route('/api', methods=['GET'])
def api():
    data = {
        'message': 'This is a sample API response!',
        'status': 'success'
    }
    return jsonify(data)

# A route that accepts POST requests
@app.route('/api/data', methods=['POST'])
def post_data():
    # Get data from the request
    input_data = request.get_json()

    # Process data (for now, we just echo it back)
    response_data = {
        'received_data': input_data
    }
    return jsonify(response_data), 201

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
