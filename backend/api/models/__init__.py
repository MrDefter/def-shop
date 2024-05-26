"""Модели валидации данных."""

from .admin import (
    AddProductModelRequest,
    AddProductModelResponse,
)

from .authentification import (
    RegistrationModelRequest,
    RegistrationModelResponse,
    AuthorizationModelResponse,
)

__all__ = [
    'AddProductModelRequest',
    'AddProductModelResponse',
    'RegistrationModelRequest',
    'RegistrationModelResponse',
    'AuthorizationModelResponse',
]
