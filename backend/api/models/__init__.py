"""Модели валидации данных."""

from .authentification import (
    RegistrationModelRequest,
    RegistrationModelResponse,
    AuthorizationModelResponse,
)

__all__ = [
    'RegistrationModelRequest',
    'RegistrationModelResponse',
    'AuthorizationModelResponse',
]
