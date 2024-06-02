"""Модели валидации данных."""

from .admin import (
    AddProductModelRequest,
    AddProductModelResponse,
    RemoveProductModelRequest,
    RemoveProductModelResponse,
)

from .authentification import (
    RegistrationModelRequest,
    RegistrationModelResponse,
    AuthorizationModelResponse,
    ExitModelResponse,
)

__all__ = [
    'AddProductModelRequest',
    'AddProductModelResponse',
    'RemoveProductModelRequest',
    'RemoveProductModelResponse',
    'RegistrationModelRequest',
    'RegistrationModelResponse',
    'AuthorizationModelResponse',
    'ExitModelResponse',
]
