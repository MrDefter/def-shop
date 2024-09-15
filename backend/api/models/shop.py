"""Модели для магазина."""

from pydantic import BaseModel, Field


class BasketModelResponse(BaseModel):
    """Модель ответа данных для авторизации."""
    message: str = Field(default_factory=str)


class CardDataModelRequest(BaseModel):
    id: str = Field(default_factory=str),