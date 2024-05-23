"""Сервис аутентификации пользователей."""

from fastapi import HTTPException, status

from backend.api.models import RegistrationModelResponse, AuthorizationModelResponse
from backend.storage import insert_data, search_user


class AuthentificationService:
    """Аутентификация пользователя"""
    def __init__(self):
        ...

    def registration_user(
        self,
        username: str,
        email: str,
        password: str,
        duplicate_password: str,
    ) -> RegistrationModelResponse:
        """Регистрация пользователя.

        Args:
            username: Имя пользователя.
            email: Майл пользователя.
            password: Пароль пользователя.
            duplicate_password: Повторный пароль пользователя.
        """
        if password != duplicate_password:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                detail='Пароли не совпадают!',
            )

        insert_data(data={'nameUser': username, 'mailUser': email, 'passwordUser': password})
        return RegistrationModelResponse(
            message='Пользователь успешно зарегистрирован!'
        )

    def authorization_user(
        self,
        email: str,
        password: str,
    ) -> AuthorizationModelResponse:
        """Авторизация пользователя."""
        search_user(data={'mailUser': email, 'passwordUser': password})
        return AuthorizationModelResponse(
            message='Вход успешно выполнен!',
        )
