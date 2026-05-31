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