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
        template: str,
        directory: str,
        request: Request,
    ) -> HTMLResponse:
        """Возвращает html шаблон для отображения на странице пользователю."""
        templates = Jinja2Templates(directory=directory)
        template = templates.TemplateResponse(template, {'request': request})
        return template

    def get_current_user(self, request: Request):
        """Тест"""
        token = request.cookies.get(get_cookies_settings().ACCESS_TOKEN)

        if not token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Вы не авторизированы!',
            )
        payload = decode(token, get_cookies_settings().SECRET_KEY, algorithms=[get_cookies_settings().ALGORITHM])

        print(payload)
