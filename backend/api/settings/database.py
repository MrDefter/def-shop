"""Настройки для postgres"""

from pydantic import Field
from pydantic_settings import BaseSettings


class PostgresSettings(BaseSettings):
    """Настройки для postgres."""
    POSTGRES_HOST: str = Field(
        description='Хост для базы данных postgres.',
        examples=['localhost'],
    )
    POSTGRES_PORT: str = Field(
        description='Порт для базы данных postgres.',
        examples=[5432],
    ),
    POSTGRES_DATABASE: str = Field(
        description='Название базы данных postgres.',
        examples=['postgres'],
    )
    POSTGRES_USER: str = Field(
        description='Юзер базы данных postgres',
        examples=['user'],
    )
    POSTGRES_PASSWORD: str = Field(
        description='Пароль для базы данных postgres',
        examples=['password'],
    )

    class Config:
        env_file = '.env'
