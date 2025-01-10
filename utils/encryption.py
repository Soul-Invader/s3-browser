from cryptography.fernet import Fernet
import os

# Load the Fernet key from the environment
FERNET_KEY = os.getenv('FERNET_KEY')

if FERNET_KEY is None:
    raise ValueError("FERNET_KEY not set in environment variables")

cipher_suite = Fernet(FERNET_KEY)

def encrypt(data):
    """Encrypt data using Fernet"""
    return cipher_suite.encrypt(data.encode()).decode()

def decrypt(data):
    """Decrypt data using Fernet"""
    return cipher_suite.decrypt(data.encode()).decode()
