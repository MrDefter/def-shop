"""Настройки."""

from .cookies import get_cookies_settings
from .database import get_postgres_settings, get_postgres_url

__all__ = ['get_cookies_settings', 'get_postgres_settings', 'get_postgres_url']
