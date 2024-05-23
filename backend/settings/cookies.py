"""Настройки для хранения cookies."""

from functools import cache

from pydantic_settings import BaseSettings
from pydantic import Field


class CookiesSettings(BaseSettings):
    """Настройки для хранение cookies."""
    SECRET_KEY: str = Field(
        description='Ключ для настройки cookis.',
        examples=['12345qwerty'],
    )
    ALGHORITM: str = Field(
        description='Алгоритм шифрования.',
        examples=['HS256'],
    )

    class Config:
        env_prefix = 'COOKIES_'


@cache
def get_cookies_settings() -> CookiesSettings:
    """Получить настройки для cookie.

    Returns:
        Настройки для cookie
    """
    return CookiesSettings()
