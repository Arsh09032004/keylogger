from utils.crypto import generate_key, save_key

key = generate_key()
save_key(key)
print("Encryption key generated and saved as key.key")
