"""Создать подключение к базе данных."""

from contextlib import contextmanager
import typing

from sqlalchemy import create_engine
from sqlalchemy.engine import Connection

from backend.settings import get_postgres_url


def get_engine() -> create_engine:
    """Получить движок базы данных postgres.

    Returns:
        Объект движка базы данных.
    """
    return create_engine(
        url=get_postgres_url(),
    )


@contextmanager
def make_cursor() -> typing.ContextManager[Connection]:
    """Создать курсов базы данных.

    Returns:
        Объект курсора.
    """

    try:
        cursor = get_engine().connect()
        try:
            yield cursor
        finally:
            cursor.close()
    finally:
        get_engine().dispose()
