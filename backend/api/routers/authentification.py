"""Регистрация и авторизация"""

from fastapi import APIRouter, Depends, Response
from fastapi.security import OAuth2PasswordRequestForm

from backend.api.models import (
    RegistrationModelRequest,
    RegistrationModelResponse,
    AuthorizationModelResponse,
)
from backend.api.service import AuthentificationService


router_authentification = APIRouter(
    tags=['Регистрация и авторизация пользователя.'],
    prefix='/authentification',
)


@router_authentification.post(
    '/registration',
    response_model=RegistrationModelResponse,
    summary='Провести регистрация пользователя.',
)
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


@router_authentification.post(
    '/authorization',
    response_model=AuthorizationModelResponse,
    summary='Провести авторизация пользователя.'
)
def post_general_authorization(
    response: Response,
    authorization_data: OAuth2PasswordRequestForm = Depends(),
    service: AuthentificationService = Depends(),
) -> AuthorizationModelResponse:
    """Провести авторизацию пользователя."""
    return service.authorization_user(
        response=response,
        username=authorization_data.username,
        password=authorization_data.password,
    )
