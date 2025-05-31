
import os
import threading
from pynput import mouse
from datetime import datetime
from utils.crypto import load_key, encrypt_message

class MouseTracker:
    def __init__(self, log_file="logs/mouse.log"):
        self.log_file = log_file
        self.key = load_key()

        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)
        with open(self.log_file, "ab") as f:
            f.write(self._encrypt_line("=== Mouse Tracking Started ==="))

    def _encrypt_line(self, line):
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        encrypted = encrypt_message(f"{timestamp} {line}", self.key)
        return encrypted + b"\n"

    def on_click(self, x, y, button, pressed):
        action = "Pressed" if pressed else "Released"
        log_line = f"Mouse {action} at ({x}, {y}) with {button}"
        with open(self.log_file, "ab") as f:
            f.write(self._encrypt_line(log_line))

    def on_scroll(self, x, y, dx, dy):
        log_line = f"Mouse scrolled at ({x}, {y}) with delta ({dx}, {dy})"
        with open(self.log_file, "ab") as f:
            f.write(self._encrypt_line(log_line))

    def start(self):
        with mouse.Listener(on_click=self.on_click, on_scroll=self.on_scroll) as listener:
            listener.join()

    def start_in_thread(self):
        t = threading.Thread(target=self.start)
        t.daemon = True
        t.start()
        print("[🖱️] Mouse tracking thread started.")
