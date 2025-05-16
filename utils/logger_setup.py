import logging
from src.config import LOG_FILE

def setup_logger():
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.DEBUG,
        format="%(asctime)s: %(message)s",
        filemode="w"
    )
