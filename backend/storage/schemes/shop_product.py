"""Схема базы данных для хранения товаров сайта."""

from sqlalchemy import Column, Integer, String

from backend.storage.schemes.config import Base


class ShopProductScheme(Base):
    """Схема базы данных для хранения товаров на сайте."""
    __tablename__ = 'shopProduct'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String, unique=False, nullable=False)
    price = Column(Integer, unique=False, nullable=False)
