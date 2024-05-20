"""Точка входа в приложение."""

import uvicorn
from argparse import ArgumentParser

from app import make_app


def main(
    host: str,
    port: int,
):
    """Точка входа в приложение.

    Args:
        host: Хост, на котором будет запущено приложение.
        port: Порт, на котором будет запущено приложение.
    """
    app = make_app()

    uvicorn.run(app, host=host, port=port)


if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument('--host', type=str, dest='host', default='127.0.0.1')
    parser.add_argument('--port', type=int, dest='port', default=8000)
    argument = parser.parse_args()

    main(argument.host, argument.port)
