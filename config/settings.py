import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME")
APP_AUTHOR = os.getenv("APP_AUTHOR")