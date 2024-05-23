"""Работы с postgres"""

from fastapi import HTTPException, status
from sqlalchemy import MetaData, Table
from sqlalchemy.exc import IntegrityError

from backend.storage.utils.connect import get_engine, make_cursor


def insert_data(table: str, data: dict) -> None:
    """Создать пользователя.

    Args:
        table: Название таблицы базы данных.
        data: Данные для вставки в базу данных.
    """
    metadata = MetaData()
    metadata.create_all(get_engine())

    table = Table(table, metadata, autoload_with=get_engine())
    insert = table.insert()

    with make_cursor() as cursor:
        try:
            cursor.execute(insert, data)
        except IntegrityError:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                detail='Такой пользователь уже существует!',
            )
