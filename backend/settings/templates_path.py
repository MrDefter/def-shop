"""Настройки путей шаблонов."""

from pydantic import Field
from pydantic_settings import BaseSettings


class TemplatesPathSettings(BaseSettings):
    TEMPLATE_GENERAL_PATH: str = Field(
        'general.html',
        description='Путь для шаблона главной страницы.',
        examples=['general.html'],
    )

    DIRECTORY_PATH: str = Field(
        'backend/templates',
        description='Директория хранения шаблонов.',
        examples=['backend/templates'],
    )


def get_templates_path_settings() -> TemplatesPathSettings:
    """Получить настройки TemplatesPathSettings"""
    return TemplatesPathSettings()
