"""Главная страница."""

from fastapi import APIRouter, Request, Depends

from backend.api.service import PagesService
from fastapi.responses import HTMLResponse

router_pages = APIRouter(
    tags=['Генерация шаблонов HTML страниц.'],
)


@router_pages.get(
    '/general',
    summary='Вернуть главную HTML страницу.',
)
def get_page_general(
        request: Request,
        service: PagesService = Depends(),
) -> HTMLResponse:
    """Вернуть главную HTML страницу.

    Args:
        request: Запрос пользователя к серверу.
        service: Сервис для работы.
    Returns:
        Сгенерированный шаблон HTML.
    """
    return service.get(
        directory='templates',
        request=request,
    )
