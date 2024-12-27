import os
import logging
from dotenv import load_dotenv

load_dotenv()

LOGGER = logging.getLogger("vassal")
if os.getenv("FLASK_ENV") == "development":
    LOGGER.setLevel(logging.DEBUG)
else:
    LOGGER.setLevel(logging.INFO)

if not LOGGER.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    LOGGER.addHandler(handler)