"""Сервис обработки html страниц."""

from fastapi import Request, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from jwt import decode

from backend.settings import get_cookies_settings


class PagesService:
    """Сервис обработки html страниц."""
    def __init__(self):
        ...

    def get(
        self,
        directory: str,
        request: Request,
    ) -> HTMLResponse:
        """Возвращает html шаблон для отображения на странице пользователю."""
        token = request.cookies.get(get_cookies_settings().ACCESS_TOKEN)
        templates = Jinja2Templates(directory=directory)

        if not token:
            template = templates.TemplateResponse('general.html', {'request': request, 'authorization': False})
            return template

        payload = decode(token, get_cookies_settings().SECRET_KEY, algorithms=[get_cookies_settings().ALGORITHM])
        template = templates.TemplateResponse(
            'general.html',
            {'request': request, 'authorization': True, 'user': payload},
        )
        return template
