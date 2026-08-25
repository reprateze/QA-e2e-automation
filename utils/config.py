import os
from dotenv import load_dotenv

load_dotenv()

FIXED_USER_EMAIL = os.getenv("FIXED_USER_EMAIL")
FIXED_USER_PASSWORD = os.getenv("FIXED_USER_PASSWORD")