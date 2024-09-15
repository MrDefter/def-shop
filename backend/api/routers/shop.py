"""Работа с магазином"""

from fastapi import APIRouter, Depends, Response, Request
from pydantic import BaseModel

from backend.api.service import ShopServices
from backend.api.models import CardDataModelRequest


router_shop = APIRouter(
    tags=['Работа с магазином'],
    prefix='/shop',
)


@router_shop.post(
    '/add_busket_product',
    summary='Добавить товар в корзину'
)
def post_general_authorization(
    card_data: CardDataModelRequest,
    user_data: Request,
    service: ShopServices = Depends(),
):
    """Провести авторизацию пользователя."""
    return service.add_busket_product(
        card_data_id=card_data.id,
        username=user_data.cookies.get('username'),
    )
