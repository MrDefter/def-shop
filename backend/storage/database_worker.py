"""Утилиты для работы с базой данных."""

from sqlalchemy import MetaData, Table

from backend.storage.utils.connect import get_engine, make_cursor


def insert_data(table: str, data: dict) -> None:
    """Вставить данные в базу данных.

    Args:
        table: Название таблицы базы данных.
        data: Данные для вставки в базу данных.
    """
    metadata = MetaData()
    metadata.create_all(get_engine())

    table = Table(table, metadata, autoload=True)
    insert = table.insert()

    with make_cursor as cursor:
        try:
            cursor.execute(insert, data)
        except Exception as exc:
            print(f'ОШИБКА: {exc}')




