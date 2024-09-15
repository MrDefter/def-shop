"""Схема базы данных для корзины сайта."""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from backend.storage.schemes.config import Base


class ShopBusketScheme(Base):
    """Схема базы данных для хранения товаров на сайте."""
    __tablename__ = 'shopBusket'

    id = Column(Integer, primary_key=True)  # Добавлен первичный ключ
    username = Column(String(), nullable=False)
    idProduct = Column(String(), nullable=False)
