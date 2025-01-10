from cryptography.fernet import Fernet

# Securely generate and store the key
KEY = Fernet.generate_key()
cipher_suite = Fernet(KEY)

def encrypt(data):
    return cipher_suite.encrypt(data.encode()).decode()

def decrypt(data):
    return cipher_suite.decrypt(data.encode()).decode()
