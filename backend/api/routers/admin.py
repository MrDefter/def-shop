"""Админский модуль."""

from fastapi import APIRouter, Depends

from backend.api.service import AdminService
from backend.api.models import AddProductModelRequest, AddProductModelResponse


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
    product_data: AddProductModelRequest,
    service: AdminService = Depends(),
) -> AddProductModelResponse:
    """Добавить товар на сайт.

    Args:
        product_data: Данные о товаре.
        service: Сервис обработки.
    """
    return service.add_product(
        name=product_data.name,
        description=product_data.description,
        price=product_data.price,
    )
