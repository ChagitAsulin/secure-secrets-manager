import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

def get_fernet():
    """טוען את מפתח ההצפנה מה-.env"""
    key = os.getenv("FERNET_KEY")
    if not key:
        raise ValueError("FERNET_KEY is not set in environment!")
    return Fernet(key.encode())

def encrypt(plain_text: str) -> str:
    """מצפין טקסט רגיל → מחרוזת מוצפנת"""
    f = get_fernet()
    return f.encrypt(plain_text.encode()).decode()

def decrypt(encrypted_text: str) -> str:
    """מפענח מחרוזת מוצפנת → טקסט רגיל"""
    f = get_fernet()
    return f.decrypt(encrypted_text.encode()).decode()