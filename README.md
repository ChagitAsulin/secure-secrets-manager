# Secure Secrets Manager

A Flask-based secure secrets manager for storing and sharing API keys and credentials.

## Features
- User registration and authentication (JWT)
- Encrypted secret storage (Fernet)
- One-time expiring share links
- Access control - users can only access their own secrets

## Setup

### Install dependencies
```bash
pip3 install -r requirements.txt
```

### Create .env file
SECRET_KEY=your-secret-key
FERNET_KEY=your-fernet-key

### Generate Fernet key
```bash
python3 -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

### Run the app
```bash
python3 app.py
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /register | Register new user |
| POST | /login | Login and get JWT token |
| POST | /secrets | Store encrypted secret |
| GET | /secrets | List all secrets |
| GET | /secrets/<id> | Get decrypted secret |
| DELETE | /secrets/<id> | Delete secret |
| POST | /secrets/<id>/share | Generate share link |
| GET | /share/<token> | Access shared secret |