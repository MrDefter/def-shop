"""Модели аутентификации пользователя."""

from pydantic import BaseModel, Field, field_validator


class RegistrationModelRequest(BaseModel):
    """Модель запроса данных для регистрации."""
    username: str = Field(default_factory=str)
    email: str = Field(default_factory=str)
    password: str = Field(default_factory=str)
    duplicate_password: str = Field(default_factory=str)

    # @field_validator('password', 'duplicate_password')
    # def validate_username(cls, password: str, duplicate_password: str) -> None:
    #     """Проверить пароль и повторение пароля на одинаковость."""
    #     test1 = password
    #     test2 = duplicate_password
    #     if password != duplicate_password:
    #         raise ValueError('ТЕСТ')


class RegistrationModelResponse(BaseModel):
    """Модель ответа на запрос данных для регистрации."""
    message: str = Field(default_factory=str)
