from datetime import datetime
import os

LOG_DIR = os.path.join(os.path.dirname(__file__), "..", "logs")
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOG_FILE = os.path.join(
    LOG_DIR, f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
)
