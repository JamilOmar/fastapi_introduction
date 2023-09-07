from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_url: str = "sqlite+aiosqlite:///./shortener.db"
    class Config:
        env_file = ".env"

def get_settings() -> Settings:
    settings = Settings()
    return settings