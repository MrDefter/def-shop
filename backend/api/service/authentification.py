"""Сервис аутентификации пользователей."""

from backend.api.models import RegistrationModelResponse
from backend.storage import insert_data


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
            return RegistrationModelResponse(
                message='Пароли не совпадают!'
            )

        data = {'nameUser': None, 'mailUser': None, 'passwordUser': None}
        insert_data(
            table='shopUsers',
            data=data,
        )

        return RegistrationModelResponse(
            message='Пользователь успешно зарегистрирован!'
        )

    def authorization_user(self):
        """Авторизация пользователя."""
        pass
