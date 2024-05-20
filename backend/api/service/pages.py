"""Сервис обработки html страниц."""

from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


class PagesService:
    """Сервис обработки html страниц."""
    def __init__(self):
        ...

    def get(
        self,
        template: str,
        directory: str,
        request: Request,
    ) -> HTMLResponse:
        """Возвращает html шаблон для отображения на странице пользователю."""
        templates = Jinja2Templates(directory=directory)
        template = templates.TemplateResponse(template, {'request': request})
        return template

