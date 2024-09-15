"""Сервис для работы с магазином"""

from backend.storage import add_busket_user


class ShopServices:
    def __init__(self):
        ...

    def add_busket_product(self, card_data_id: str, username: str):
        """Добавить товар в корзину"""
        data = {"username": username, "idProduct": card_data_id}
        add_busket_user(data=data)
        return 'Успешно'
