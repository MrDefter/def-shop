"""Работа с магазином"""

from fastapi import APIRouter, Depends, Response, Request

from backend.api.service import ShopServices
from fastapi.security import OAuth2PasswordRequestForm


router_shop = APIRouter(
    tags=['Работа с магазином'],
    prefix='/shop',
)


@router_shop.post(
    '/add_busket_product',
    summary='Добавить товар в корзину'
)
def post_general_authorization(
    user_data: Request,
    card_data,
    response: Response,
    service: ShopServices = Depends(),
):
    """Провести авторизацию пользователя."""
    print(card_data)
    return service.add_busket_product(
        username=user_data.cookies.get('username'),
    )

