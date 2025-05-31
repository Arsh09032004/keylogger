from utils.crypto import load_key, decrypt_message

def decrypt_mouse_logs(log_file="logs/mouse.log"):
    key = load_key()

    print("Decrypted Mouse Logs:\n")
    with open(log_file, "rb") as f:
        for i, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                decrypted = decrypt_message(line, key)
                print(decrypted)
            except Exception:
                print(f"[Line {i}] ❌ Could not decrypt.")

if __name__ == "__main__":
    decrypt_mouse_logs()
