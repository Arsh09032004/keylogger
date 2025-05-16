from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def save_key(key, filepath="key.key"):
    with open(filepath, "wb") as f:
        f.write(key)

def load_key(filepath="key.key"):
    with open(filepath, "rb") as f:
        return f.read()

def encrypt_message(message: str, key: bytes) -> bytes:
    f = Fernet(key)
    return f.encrypt(message.encode())

def decrypt_message(encrypted: bytes, key: bytes) -> str:
    f = Fernet(key)
    return f.decrypt(encrypted).decode()
