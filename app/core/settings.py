from functools import lru_cache

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv(".env")


class Settings(BaseSettings):
    app_version: str
    app_v1_prefix: str
    project_name: str
    project_description: str

    mongodb_uri: str
    mongodb_name: str

    class Config:
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
