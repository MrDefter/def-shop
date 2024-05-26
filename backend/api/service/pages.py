"""Сервис обработки html страниц."""

from fastapi import Request, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from jwt import decode

from backend.settings import get_cookies_settings
from backend.storage import check_admin, get_product


class PagesService:
    """Сервис обработки html страниц."""
    def __init__(self):
        ...

    def __get_token(self, request) -> str:
        """Получить токен пользователя.

        Args:
            request: Запрос пользователя.
        """
        return request.cookies.get(get_cookies_settings().ACCESS_TOKEN)

    def __check_token(self, token: str | None) -> bool:
        """Проверить токен для авторизации.

        Args:
            token: Токен пользователя.
        Returns:
            True, если токен существует. Иначе False.
        """
        return bool(token)

    def __check_admin(self, token: str | None) -> bool:
        """Проверить, является ли пользователь администратором.

        Args:
            token: Токен пользователя.
        Returns:
            True, если пользователь администратор. Иначе False
        """
        payload = decode(token, get_cookies_settings().SECRET_KEY, algorithms=[get_cookies_settings().ALGORITHM])
        return check_admin(payload)

    def __get_products(self) -> list:
        """Получить список товаров магазина.

        Returns:
            Список товаров магазина.
        """
        products = get_product()
        return products

    def get(
        self,
        directory: str,
        request: Request,
    ) -> HTMLResponse:
        """Возвращает html шаблон для отображения на странице пользователю."""
        templates = Jinja2Templates(directory=directory)
        token = self.__get_token(request)
        data = {'request': request, 'authorization': False, 'is_admin': False}

        products = get_product()
        print(products)

        if self.__check_token(token=token):
            data['authorization'] = True
        if self.__check_token(token=token):
            data['is_admin'] = True
        data['products'] = self.__get_products()

        template = templates.TemplateResponse('general.html', data)
        return template
