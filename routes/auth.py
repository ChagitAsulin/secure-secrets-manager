from flask import Blueprint, request, jsonify
from models.user import create_user, find_user_by_username, check_password
from utils.auth import generate_token

auth_bp = Blueprint("auth", __name__) 

@auth_bp.route("/register", methods=["POST"])
def register():
    """Register a new user"""
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    username = data.get("username", "").strip()
    password = data.get("password", "")

    # Input validation
    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    if len(username) < 3 or len(username) > 50:
        return jsonify({"error": "Username must be between 3 and 50 characters"}), 400

    if len(password) < 6:
        return jsonify({"error": "Password must be at least 6 characters"}), 400

    user = create_user(username, password)
    if not user:
        return jsonify({"error": "Username already exists"}), 409

    return jsonify({"message": "User created successfully", "id": user["id"]}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    """Authenticate an existing user and return a JWT token"""
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = find_user_by_username(username)
    if not user or not check_password(user, password):
        return jsonify({"error": "Invalid credentials"}), 401

    token = generate_token(user["id"])
    return jsonify({"token": token}), 200