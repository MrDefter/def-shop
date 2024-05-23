"""Модели валидации данных."""

from .authentification import (
    RegistrationModelRequest,
    RegistrationModelResponse,
    AuthorizationModelRequest,
    AuthorizationModelResponse,
)

__all__ = [
    'RegistrationModelRequest',
    'RegistrationModelResponse',
    'AuthorizationModelRequest',
    'AuthorizationModelResponse',
]
