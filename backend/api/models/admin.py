"""Модели админского модуля."""

from pydantic import BaseModel, Field


class AddProductModelRequest(BaseModel):
    """Модель запроса добавления товара в магазин."""
    name: str = Field(default_factory=str)
    description: str = Field(default_factory=str)
    price: int = Field(default_factory=int)


class AddProductModelResponse(BaseModel):
    """Модель ответа добавления товара в магазин."""
    message: str = Field(default_factory=str)


class RemoveProductModelRequest(BaseModel):
    """Модель запроса удаления товара из магазина."""
    product_id: int = Field(default_factory=int)


class RemoveProductModelResponse(BaseModel):
    """Модель ответа удаления товара из магазина."""
    message: str = Field(default_factory=str)
