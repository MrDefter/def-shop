"""Сервис аутентификации пользователей."""

from backend.api.models import RegistrationModelResponse


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
        """

        if password != duplicate_password:
            return RegistrationModelResponse(
                message='Пароли не совпадают!'
            )

        print(username, email, password)
        return RegistrationModelResponse(
            message='Пользователь успешно зарегистрирован!'
        )

    def authorization_user(self):
        """Авторизация пользователя."""
        pass
