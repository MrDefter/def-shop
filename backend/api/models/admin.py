"""Модели админского модуля."""

from pydantic import BaseModel, Field


class AddProductModelRequest(BaseModel):
    """Модель запроса добавления товара в магазин."""
    name: str = Field(default_factory=str)
    description: str = Field(default_factory=str)
    price: int = Field(default_factory=int)


class AddProductModelResponse(BaseModel):
    message: str = Field(default_factory=str)
