"""Регистрация и авторизация"""

from fastapi import APIRouter, Depends

from backend.api.models import (
    RegistrationModelRequest,
    RegistrationModelResponse,
    AuthorizationModelRequest,
    AuthorizationModelResponse,
)
from backend.api.service import AuthentificationService


router_authentification = APIRouter(
    tags=['Регистрация и авторизация пользователя.'],
    prefix='/authentification',
)


@router_authentification.post('/registration')
def post_general_registration(
    registration_data: RegistrationModelRequest,
    service: AuthentificationService = Depends(),
) -> RegistrationModelResponse:
    """Провести регистрация пользователя."""
    return service.registration_user(
        username=registration_data.username,
        email=registration_data.email,
        password=registration_data.password,
        duplicate_password=registration_data.duplicate_password,
    )


@router_authentification.post('/authorization')
def post_general_authorization(
    authorization_data: AuthorizationModelRequest,
    service: AuthentificationService = Depends(),
):
    """Провести авторизацию пользователя."""
    return service.authorization_user(
        email=authorization_data.email,
        password=authorization_data.password,
    )
