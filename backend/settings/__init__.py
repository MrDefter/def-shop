"""Настройки."""

from .templates_path import get_templates_path_settings
from .database import get_postgres_settings, get_postgres_url

__all__ = ['get_postgres_settings', 'get_postgres_url']
