import json
import os
import uuid
from datetime import datetime, timedelta

DATA_DIR = "data/tokens"

def _token_path(token):
    return os.path.join(DATA_DIR, f"{token}.json")

def create_token(secret_id, expires_in_minutes=60):
    """Create a one-time expiring share token"""
    os.makedirs(DATA_DIR, exist_ok=True)

    token = str(uuid.uuid4())
    expires_at = (datetime.utcnow() + timedelta(minutes=expires_in_minutes)).isoformat()

    data = {
        "token": token,
        "secret_id": secret_id,
        "expires_at": expires_at,
        "used": False
    }

    with open(_token_path(token), "w") as f:
        json.dump(data, f)

    return token

def get_and_consume_token(token):
    """Return token data and mark it as used - one time only"""
    path = _token_path(token)
    if not os.path.exists(path):
        return None

    with open(path) as f:
        data = json.load(f)

    if datetime.utcnow() > datetime.fromisoformat(data["expires_at"]):
        return None

    if data["used"]:
        return None

    data["used"] = True
    with open(path, "w") as f:
        json.dump(data, f)

    return data