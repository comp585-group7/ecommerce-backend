from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello from your Flask API!'})

@app.route('/', methods=['GET'])  # Add this route
def index():
    return "Welcome to the API!"

if __name__ == '__main__':
    app.run(debug=True)