from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory storage (temporary)
users = []

@app.route('/api/submit', methods=['POST'])
def submit_form():
    data = request.json
    users.append(data)

    return jsonify({
        "message": "Data Successfully Saved"
    }), 201


@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "Backend is running"
    }), 200


@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
