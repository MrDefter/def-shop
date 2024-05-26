"""Сервис для работы с админской панелью."""

from backend.api.models import AddProductModelResponse
from backend.storage import insert_product


class AdminService:
    def __init__(self):
        ...

    def add_product(self, name, description, price) -> AddProductModelResponse:
        """Добавить товар в магазин.

        Args:
            name: Название товара.
            description: Описание товара.
            price: Цена товара.
        """
        insert_product(data={"name": name, "description": description, "price": price})

        return AddProductModelResponse(
            message='Товар успешно добавлен!',
        )
