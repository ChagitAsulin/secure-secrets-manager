import json
import os
import uuid
from datetime import datetime

DATA_DIR = "data/secrets"

def _secret_path(secret_id):
    return os.path.join(DATA_DIR, f"{secret_id}.json")

def create_secret(user_id, name, encrypted_value, description=""):
    """Save an encrypted secret to file"""
    os.makedirs(DATA_DIR, exist_ok=True)

    secret_id = str(uuid.uuid4())
    secret = {
        "id": secret_id,
        "user_id": user_id,
        "name": name,
        "description": description,
        "encrypted_value": encrypted_value,
        "created_at": datetime.utcnow().isoformat()
    }

    with open(_secret_path(secret_id), "w") as f:
        json.dump(secret, f)

    return secret

def get_secret(secret_id):
    """Get a secret by ID"""
    path = _secret_path(secret_id)
    if not os.path.exists(path):
        return None

    with open(path) as f:
        return json.load(f)

def update_secret(secret_id, name=None, description=None):
    """Update secret metadata"""
    secret = get_secret(secret_id)
    if not secret:
        return None

    if name:
        secret["name"] = name
    if description:
        secret["description"] = description

    with open(_secret_path(secret_id), "w") as f:
        json.dump(secret, f)

    return secret

def delete_secret(secret_id):
    """Delete a secret file"""
    path = _secret_path(secret_id)
    if os.path.exists(path):
        os.remove(path)
        return True
    return False

def list_secrets_for_user(user_id):
    """List all secrets for a user without exposing encrypted values"""
    if not os.path.exists(DATA_DIR):
        return []

    results = []
    for filename in os.listdir(DATA_DIR):
        with open(os.path.join(DATA_DIR, filename)) as f:
            secret = json.load(f)
            if secret["user_id"] == user_id:
                safe = {k: v for k, v in secret.items() if k != "encrypted_value"}
                results.append(safe)
    return results