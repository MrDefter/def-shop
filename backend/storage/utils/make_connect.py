from psycopg2 import connect

from backend.settings import get_postgres_settings


def make_connect() -> connect:
    """Создать подключение к базе данных."""
    return connect(
        dbname=get_postgres_settings().POSTGRES_NAME,
        user=get_postgres_settings().POSTGRES_USER,
        password=get_postgres_settings().POSTGRES_PASSWORD,
        host=get_postgres_settings().POSTGRES_HOST,
        port=get_postgres_settings().POSTGRES_PORT,
    )
