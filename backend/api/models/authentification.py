"""Модели аутентификации пользователя."""

from pydantic import BaseModel, Field


class RegistrationModelRequest(BaseModel):
    """Модель запроса данных для регистрации."""
    username: str = Field(default_factory=str)
    email: str = Field(default_factory=str)
    password: str = Field(default_factory=str)
    duplicate_password: str = Field(default_factory=str)


class RegistrationModelResponse(BaseModel):
    """Модель ответа на запрос данных для регистрации."""
    message: str = Field(default_factory=str)


class AuthorizationModelResponse(BaseModel):
    """Модель ответа данных для авторизации."""
    message: str = Field(default_factory=str)


class ExitModelResponse(BaseModel):
    message: str = Field(default_factory=str)
