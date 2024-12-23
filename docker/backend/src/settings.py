from typing import Set
import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = os.environ['APP_NAME']
    APP_VERSION: str = os.environ['APP_VERSION']
    POSTGRESQL_HOSTNAME: str = os.environ['POSTGRES_HOST']
    POSTGRESQL_HOSTNAME_DOCKER: str = os.environ['POSTGRES_HOST_DOCKER']
    POSTGRESQL_USERNAME: str = os.environ['POSTGRES_USER']
    POSTGRESQL_PASSWORD: str = os.environ['POSTGRES_PASSWORD']
    POSTGRESQL_DATABASE: str = os.environ['POSTGRES_DB']


settings = Settings()