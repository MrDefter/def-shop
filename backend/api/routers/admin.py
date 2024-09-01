"""Админский модуль."""

from fastapi import APIRouter, Depends, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse

from backend.api.service import AdminService
from backend.api.models import (
    AddProductModelRequest,
    AddProductModelResponse,
    RemoveProductModelRequest,
    RemoveProductModelResponse,
)


router_admin = APIRouter(
    tags=['Админиский модуль для управления товарами и пользователями.'],
    prefix='/admin',
)


@router_admin.post(
    '/add_product',
    response_model=AddProductModelResponse,
    summary='Добавить товар в магазин.',
)
def post_add_product(
    name: str = Form(...),
    description: str = Form(...),
    price: int = Form(...),
    file: UploadFile = File(...),
    service: AdminService = Depends(),
) -> AddProductModelResponse:
    """Добавить товар на сайт.

    Args:
        name: Название товара.
        description: Описание товара.
        price: Цена товара.
        file: Файл.
        service: Сервис обработки.
    """
    return service.add_product(
        name=name,
        description=description,
        price=price,
        file=file
    )


@router_admin.post(
    '/remove_product',
    response_model=RemoveProductModelRequest,
    summary='Удалить товар.'
)
def post_remove_product(
    product_data: RemoveProductModelRequest,
    service: AdminService = Depends(),
) -> RemoveProductModelResponse:
    """Удалить товар."""
    return service.remove_product(
        product_id=product_data.product_id,
    )


@router_admin.get(
    '/get_product',
    summary='Получить html шаблон товаров.',
)
def get_get_product(
    request: Request,
    service: AdminService = Depends(),
) -> HTMLResponse:
    return service.get_product(
        directory='templates/_ajax',
        request=request,
    )
