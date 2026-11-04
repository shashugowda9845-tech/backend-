
from flask import Flask, request, jsonify
import re

app = Flask(__name__)


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    name = data.get('name', '')
    email = data.get('email', '')

    if not name or not email:
        return jsonify({
            "success": False,
            "message": "Name and Email are required"
        }), 400

    if not is_valid_email(email):
        return jsonify({
            "success": False,
            "message": "Invalid Email format"
        }), 400

    return jsonify({
        "success": True,
        "message": f"User {name} registered successfully with {email}"
    }), 200


if __name__ == '__main__':
    app.run(debug=True)
