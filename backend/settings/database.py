"""Настройки для postgres"""

from functools import cache

from pydantic import Field
from pydantic_settings import BaseSettings
from sqlalchemy.engine import URL


class PostgresSettings(BaseSettings):
    """Настройки для postgres."""
    HOST: str = Field(
        description='Хост для базы данных postgres.',
        examples=['localhost'],
    )
    PORT: int = Field(
        description='Порт для базы данных postgres.',
        examples=[5432],
    )
    DATABASE: str = Field(
        description='Название базы данных postgres.',
        examples=['postgres'],
    )
    USER: str = Field(
        description='Юзер базы данных postgres',
        examples=['user'],
    )
    PASSWORD: str = Field(
        description='Пароль для базы данных postgres',
        examples=['password'],
    )

    class Config:
        env_prefix = 'POSTGRES_'


@cache
def get_postgres_settings() -> PostgresSettings:
    """Получить настройки для postgres.

    Returns:
        настройки для базы данных postgres.
    """
    return PostgresSettings()


@cache
def get_postgres_url() -> URL:
    """Получить настройки url для postgres.

    Returns:
        Настройки url Для базы данных postgres.
    """
    settings = get_postgres_settings()
    return URL(
        drivername='postgresql',
        database=settings.DATABASE,
        username=settings.USER,
        password=settings.PASSWORD,
        host=settings.HOST,
        port=settings.PORT,
        query={},
    )
