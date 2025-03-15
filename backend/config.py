from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Application configurations
SECRET_KEY = os.getenv("SECRET_KEY", "your_default_secret_key")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///database/medical_assistant.db")
DEBUG = os.getenv("DEBUG", "True") == "True"

# Other potential settings
SQLALCHEMY_TRACK_MODIFICATIONS = False

