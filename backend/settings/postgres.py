"""Настройки для Postgres."""

from pydantic import Field
from pydantic_settings import BaseSettings


class PostgresSettings(BaseSettings):
    """Настройки для Postgres."""
    POSTGRES_NAME: str = Field(
        'database',
        description='Название базы данных.',
        examples=['database'],
    )
    POSTGRES_USER: str = Field(
        'user',
        description='Юзер базы данных.',
        examples=['user'],
    )
    POSTGRES_PASSWORD: str = Field(
        'password',
        description='Пароль базы данных.',
        examples=['password'],
    )
    POSTGRES_HOST: str = Field(
        'localhost',
        description='Хост базы данных.',
        examples=['localhost'],
    )
    POSTGRES_PORT: str = Field(
        '5432',
        description='Порт базы данных.',
        examples=['5432'],
    )


def get_postgres_settings() -> PostgresSettings:
    """Получить конфигурацию postgres.

    Returns:
        Конфигурация postgres.
    """
    return PostgresSettings()
