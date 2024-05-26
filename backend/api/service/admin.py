"""Сервис для работы с админской панелью."""

from backend.api.models import AddProductModelResponse


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

        print(name, description, price)
        return AddProductModelResponse(
            message='Тест',
        )
