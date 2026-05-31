import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "change-me-in-production")
    FERNET_KEY = os.getenv("FERNET_KEY")
    DATA_DIR = "data"