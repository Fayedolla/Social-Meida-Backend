from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

# Get the current directory (app folder)
BASE_DIR = Path(__file__).resolve().parent

class Settings(BaseSettings):
    DATABASE_HOSTNAME: str
    DATABASE_PORT: str
    DATABASE_PASSWORD: str
    DATABASE_NAME: str
    DATABASE_USERNAME: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    model_config = SettingsConfigDict(
        env_file = str(BASE_DIR / ".env"),
        case_sensitive=True
    )

settings = Settings()