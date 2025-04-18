from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()  # Load from .env

class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()
