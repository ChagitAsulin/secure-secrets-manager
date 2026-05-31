from flask import Blueprint, request, jsonify
from models.secret import create_secret, get_secret, update_secret, delete_secret, list_secrets_for_user
from utils.auth import require_auth
from utils.encryption import encrypt, decrypt

secrets_bp = Blueprint("secrets", __name__)

@secrets_bp.route("/secrets", methods=["POST"])
@require_auth
def store_secret():
    """Store a new encrypted secret"""
    data = request.get_json()
    name = data.get("name")
    value = data.get("value")
    description = data.get("description", "")

    if not name or not value:
        return jsonify({"error": "Name and value are required"}), 400

    encrypted_value = encrypt(value)
    secret = create_secret(request.user_id, name, encrypted_value, description)
    return jsonify({"message": "Secret stored successfully", "id": secret["id"]}), 201


@secrets_bp.route("/secrets", methods=["GET"])
@require_auth
def list_secrets():
    """List all secrets for the authenticated user (without values)"""
    secrets = list_secrets_for_user(request.user_id)
    return jsonify(secrets), 200


@secrets_bp.route("/secrets/<secret_id>", methods=["GET"])
@require_auth
def get_secret_by_id(secret_id):
    """Retrieve and decrypt a specific secret"""
    secret = get_secret(secret_id)

    if not secret:
        return jsonify({"error": "Secret not found"}), 404

    # Only the owner can access their secret
    if secret["user_id"] != request.user_id:
        return jsonify({"error": "Access denied"}), 403

    secret["value"] = decrypt(secret["encrypted_value"])
    del secret["encrypted_value"]
    return jsonify(secret), 200


@secrets_bp.route("/secrets/<secret_id>", methods=["PUT"])
@require_auth
def update_secret_by_id(secret_id):
    """Update secret metadata (name or description)"""
    secret = get_secret(secret_id)

    if not secret:
        return jsonify({"error": "Secret not found"}), 404

    if secret["user_id"] != request.user_id:
        return jsonify({"error": "Access denied"}), 403

    data = request.get_json()
    updated = update_secret(secret_id, data.get("name"), data.get("description"))
    return jsonify(updated), 200


@secrets_bp.route("/secrets/<secret_id>", methods=["DELETE"])
@require_auth
def delete_secret_by_id(secret_id):
    """Delete a secret"""
    secret = get_secret(secret_id)

    if not secret:
        return jsonify({"error": "Secret not found"}), 404

    if secret["user_id"] != request.user_id:
        return jsonify({"error": "Access denied"}), 403

    delete_secret(secret_id)
    return jsonify({"message": "Secret deleted successfully"}), 200