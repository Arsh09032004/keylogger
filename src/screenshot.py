import os
import threading
import time
from datetime import datetime
from PIL import ImageGrab
import json

class ScreenshotCapturer:
    def __init__(self, folder="screenshots", config_path="config.json"):
        self.folder = folder
        self.config_path = config_path
        self.interval = self.load_interval()
        os.makedirs(self.folder, exist_ok=True)

    def load_interval(self):
        try:
            with open(self.config_path, "r") as f:
                config = json.load(f)
            interval = int(config.get("screenshot_interval", 10))
            return max(1, interval)  # prevent 0 or negative values
        except Exception as e:
            print(f"[⚠️] Failed to load config: {e}")
            return 10  # fallback

    def capture_loop(self):
        while True:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filepath = os.path.join(self.folder, f"screenshot_{timestamp}.png")
            try:
                img = ImageGrab.grab()
                img.save(filepath)
                print(f"[📸] Screenshot saved: {filepath}")
            except Exception as e:
                print(f"[❌] Screenshot failed: {e}")
            time.sleep(self.interval)

    def start_in_thread(self):
        t = threading.Thread(target=self.capture_loop)
        t.daemon = True
        t.start()
        print("[🖼️] Screenshot capturing thread started.")
