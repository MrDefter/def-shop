"""Работы с postgres"""

from fastapi import HTTPException, status
from sqlalchemy import insert, select
from sqlalchemy.exc import IntegrityError

from backend.storage.utils.connect import make_cursor
from backend.storage.schemes import ShopUsersScheme


def insert_data(data: dict) -> None:
    """Создать пользователя.

    Args:
        data: Данные для вставки в базу данных.
    """
    query = insert(ShopUsersScheme)

    with make_cursor() as cursor:
        try:
            cursor.execute(query, data)
        except IntegrityError as exc:
            print(exc)
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                detail='Такой пользователь уже существует!',
            )


def search_user(data: dict) -> bool:
    """Найти пользователя.

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
