"""Работы с postgres"""

from sqlalchemy import MetaData, Table, insert

from backend.storage.utils.postgres_connect import get_engine, make_cursor


def insert_data(table: str, data: dict) -> None:
    """Вставить данные в базу данных.

    Args:
        table: Название таблицы базы данных.
        data: Данные для вставки в базу данных.
    """
    metadata = MetaData()
    metadata.create_all(get_engine())

    table = Table(table, metadata, autoload_with=get_engine())
    stmt = insert(table).values(data)

    print(stmt)
    with make_cursor() as cursor:
        # try:
        cursor.execute(stmt)
        # except Exception as exc:
        #     print(f'ОШИБКА: {exc}')
