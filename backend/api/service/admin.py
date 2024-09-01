"""Сервис для работы с админской панелью."""

from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from backend.api.models import AddProductModelResponse, RemoveProductModelResponse
from backend.storage import insert_product, get_products, remove_product


class AdminService:
    def __init__(self):
        ...

    def __get_products(self) -> list:
        """Получить список товаров магазина.

        Returns:
            Список товаров магазина.
        """
        products = get_products()
        return products

    def __save_winrar(self, file) -> list:
        pass
    
    def add_product(self, name: str, description: str, price: int, file) -> AddProductModelResponse:
        """Добавить товар в магазин.

        Args:
            name: Название товара.
            description: Описание товара.
            price: Цена товара.
            file: Файл.
        """
        insert_product(data={"name": name, "description": description, "price": price})

        return AddProductModelResponse(
            message='Товар успешно добавлен!',
        )
    
    def remove_product(self, product_id: int) -> RemoveProductModelResponse:
        """Удалить товар из магазина.
        
        Args:
            product_id: Идентификационный номер товара.
        """
        remove_product(product_id=product_id)
        return RemoveProductModelResponse(
            message='Успешное удаление.',
        )

    def get_product(self, directory: str, request: Request) -> HTMLResponse:
        """Отобразить товары.

        Args:
            directory: Код до директории с шаблонами.
            request: Запрос пользователя.
        """
        templates = Jinja2Templates(directory=directory)

        data = {'request': request, 'products': self.__get_products()}
        print(data)
        template = templates.TemplateResponse('get_product.html', data)
        return template
