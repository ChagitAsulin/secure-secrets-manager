from flask import Blueprint, request, jsonify
from models.secret import get_secret
from models.share_token import create_token, get_and_consume_token
from utils.auth import require_auth
from utils.encryption import decrypt

share_bp = Blueprint("share", __name__)

@share_bp.route("/secrets/<secret_id>/share", methods=["POST"])
@require_auth
def generate_share_link(secret_id):
    """Generate a one-time expiring share link for a secret"""
    secret = get_secret(secret_id)

    if not secret:
        return jsonify({"error": "Secret not found"}), 404

    if secret["user_id"] != request.user_id:
        return jsonify({"error": "Access denied"}), 403

    expires_in = request.get_json().get("expires_in_minutes", 60)
    token = create_token(secret_id, expires_in)

    return jsonify({
        "share_url": f"/share/{token}",
        "expires_in_minutes": expires_in
    }), 201


@share_bp.route("/share/<token>", methods=["GET"])
def access_shared_secret(token):
    """Access a secret via a one-time share token"""
    token_data = get_and_consume_token(token)

    if not token_data:
        return jsonify({"error": "Token is invalid, expired, or already used"}), 404

    secret = get_secret(token_data["secret_id"])
    if not secret:
        return jsonify({"error": "Secret not found"}), 404

    return jsonify({
        "name": secret["name"],
        "value": decrypt(secret["encrypted_value"])
    }), 200