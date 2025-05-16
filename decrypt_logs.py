from cryptography.fernet import Fernet

def load_key(filepath="key.key"):
    """Load the encryption key from a file"""
    with open(filepath, "rb") as f:
        return f.read()

def decrypt_log(log_file="logs/keystrokes.log", key_file="key.key"):
    key = load_key(key_file)
    fernet = Fernet(key)
    
    with open(log_file, "rb") as f:
        encrypted_lines = f.readlines()

    print("Decrypted keystrokes:")
    for encrypted_line in encrypted_lines:
        try:
            decrypted = fernet.decrypt(encrypted_line.strip())
            print(decrypted.decode())  # decode bytes to string
        except Exception as e:
            print(f"Failed to decrypt a line: {e}")

if __name__ == "__main__":
    decrypt_log()
