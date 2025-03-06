from pydantic import ConfigDict
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BOT_TOKEN: str
    ENVIRONMENT: str
    
    model_config = ConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        cache_strings=False,
        case_sensitive=True
    )
    
    
settings = Settings()