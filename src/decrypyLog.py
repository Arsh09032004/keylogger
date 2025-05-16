from utils.crypto import load_key, decrypt_message

def view_log(file_path="logs/your_encrypted_file.txt"):
    key = load_key()
    with open(file_path, "rb") as f:
        for line in f:
            try:
                print(decrypt_message(line.strip(), key))
            except:
                print("Decryption failed for a line")

if __name__ == "__main__":
    view_log()
