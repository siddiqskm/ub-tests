from pydantic import (BaseSettings, AnyUrl)


class Settings(BaseSettings):
    author_service_url: AnyUrl
    search_service_url: AnyUrl
    proxy_service_url: AnyUrl
    test_data_file: str

    class Config:
        env_file = ".env"

Config = Settings()