"""Главная страница."""

from fastapi import APIRouter, Request, Depends

from backend.api.service import PagesService
from backend.settings import get_templates_path_settings
from fastapi.responses import HTMLResponse


router_pages = APIRouter(
    tags=['Генерация шаблонов HTML страниц.'],
)


@router_pages.get('/general')
def get_page_general(
        request: Request,
        service: PagesService = Depends(),
) -> HTMLResponse:
    """Вернуть главную HTML страницу.

    Args:
        request: Запрос пользователя к серверу.
        service: HTML шаблон.
    Returns:
        Сгенерированный шаблон HTML.
    """
    return service.get(
        template=get_templates_path_settings().TEMPLATE_GENERAL_PATH,
        directory=get_templates_path_settings().DIRECTORY_PATH,
        request=request,
    )
