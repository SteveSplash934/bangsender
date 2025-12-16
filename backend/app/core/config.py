from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from pathlib import Path

# Move up from: backend/app/core/config.py -> backend/ -> root/
PROJECT_DIR = Path(__file__).resolve().parent.parent.parent.parent

class Settings(BaseSettings):
    """
    Centralized configuration management.
    Validates environment variables on startup.
    """
    
    # App Info
    APP_NAME: str = "NovaMailer"
    API_V1_STR: str = "/api/v1"
    MODE: str = "dev" # dev, prod, test
    
    # Database (PostgreSQL)
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str
    
    # Redis
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379

    # Security
    SECRET_KEY: str

    model_config = SettingsConfigDict(
        env_file=f"{PROJECT_DIR}/.env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )

    @property
    def DATABASE_URL(self) -> str:
        """Async connection string for SQLAlchemy"""
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

@lru_cache
def get_settings():
    return Settings()

settings = get_settings()