import json
import os
import uuid
import bcrypt

DATA_DIR = "data/users"

def _user_path(user_id):
    return os.path.join(DATA_DIR, f"{user_id}.json")

def create_user(username, password):
    """Create a new user and save to file"""
    os.makedirs(DATA_DIR, exist_ok=True)

    if find_user_by_username(username):
        return None

    user_id = str(uuid.uuid4())
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    user = {
        "id": user_id,
        "username": username,
        "password_hash": hashed
    }

    with open(_user_path(user_id), "w") as f:
        json.dump(user, f)

    return user

def find_user_by_username(username):
    """Find a user by username"""
    if not os.path.exists(DATA_DIR):
        return None

    for filename in os.listdir(DATA_DIR):
        with open(os.path.join(DATA_DIR, filename)) as f:
            user = json.load(f)
            if user["username"] == username:
                return user
    return None

def check_password(user, password):
    """Verify user password against stored hash"""
    return bcrypt.checkpw(password.encode(), user["password_hash"].encode())