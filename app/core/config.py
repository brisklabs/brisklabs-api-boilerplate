import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file

class Settings:
    PROJECT_NAME: str = "Brisklabs API Boilerplate"
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

settings = Settings()
