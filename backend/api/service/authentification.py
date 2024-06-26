"""Сервис аутентификации пользователей."""

from fastapi import HTTPException, status, Response
from jwt import encode

from backend.api.models import RegistrationModelResponse, AuthorizationModelResponse, ExitModelResponse
from backend.storage import insert_user, check_user
from backend.settings import get_cookies_settings


class AuthentificationService:
    """Аутентификация пользователя"""
    def __init__(self):
        ...

    def __create_access_token_login(self, data: dict):
        """Создать токен авторизации пользователя.

        Args:
            data: Некоторые данные о пользователе.
        """
        encoded_jwt = encode(data, get_cookies_settings().SECRET_KEY, get_cookies_settings().ALGORITHM)
        return encoded_jwt

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
        Returns:
            Сообщение.
        """
        if password != duplicate_password:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, detail='Пароли не совпадают!')

        insert_user(data={'username': username, 'email': email, 'password': password})
        return RegistrationModelResponse(message='Пользователь успешно зарегистрирован!')

    def authorization_user(
        self,
        response: Response,
        username: str,
        password: str,
    ) -> AuthorizationModelResponse:
        """Авторизация пользователя."""
        if check_user(data={'username': username, 'password': password}):
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                detail='Пользователь не найден! Проверьте правильность указанных данных.'
            )

        access_token = self.__create_access_token_login(data={'sub': username})
        response.set_cookie(
            key=get_cookies_settings().ACCESS_TOKEN,
            value=access_token,
            httponly=True,
            max_age=3600,
        )
        return AuthorizationModelResponse(message='Вход успешно выполнен!')

    def exit_user(self, user_data: Response) -> ExitModelResponse:
        """Провести выход пользователя.

        Args:
            user_data: Данные пользователя пользователя.
        Returns:
            Ответ.
        """
        user_data.delete_cookie(key=get_cookies_settings().ACCESS_TOKEN)
        return ExitModelResponse(
            message='Выход успешно выполнен.'
        )
