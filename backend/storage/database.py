"""Работы с postgres"""

from fastapi import HTTPException, status
from sqlalchemy import insert, select, delete
from sqlalchemy.exc import IntegrityError

from backend.storage.utils.connect import make_cursor
from backend.storage.schemes import ShopProductScheme, ShopUsersScheme


def insert_user(data: dict) -> None:
    """Создать пользователя.

    Args:
        data: Данные для вставки в базу данных.
    """
    query = insert(ShopUsersScheme)

    with make_cursor() as cursor:
        try:
            cursor.execute(query, data)
        except IntegrityError:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                detail='Такой пользователь уже существует!',
            )


def insert_product(data: dict) -> None:
    """Создать товар.

    Args:
        data: Информация о товаре.
    """
    query = insert(ShopProductScheme)

    with make_cursor() as cursor:
        try:
            cursor.execute(query, data)
        except IntegrityError:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                detail='Такое название товара уже существует!',
            )


def remove_product(product_id: int) -> None:
    """Удалить товар из базы данных.

    Args:
        product_id: Идентификационный номер, по которому произвести удаление.
    """
    query = delete(ShopProductScheme).where(ShopProductScheme.id == product_id)

    with make_cursor() as cursor:
        cursor.execute(query)


def get_products() -> list:
    """Получить все товары.

    Retuns:
        Список товаров.
    """
    query = select(
        ShopProductScheme.id,
        ShopProductScheme.name,
        ShopProductScheme.description,
        ShopProductScheme.price,
    )

    with make_cursor() as cursor:
        products = cursor.execute(query).all()
        return products


def check_user(data: dict) -> bool:
    """Имеется ли такой пользователь.

    Returns:
        True, если пользователь найден. Иначе False.
    """
    query = select(ShopUsersScheme).where(
        ShopUsersScheme.username == data['username'],
        ShopUsersScheme.password == data['password'],
    )

    with make_cursor() as cursor:
        user = cursor.execute(query).all()
        return not len(user)


def check_admin(data: dict) -> bool:
    """Является ли пользователь администратором.

    Returns:
        True, если пользователь является администратором. Иначе False.
    """
    query = select(ShopUsersScheme.isAdmin).where(
        ShopUsersScheme.username == data['sub'],
    )

    with make_cursor() as cursor:
        return cursor.execute(query).all()[0][0]
