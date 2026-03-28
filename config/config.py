import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

BASE_URL: Optional[str] = os.getenv("BASE_URL")
API_KEY: Optional[str] = os.getenv("API_KEY")
UI_URL: Optional[str] = os.getenv("UI_URL")
