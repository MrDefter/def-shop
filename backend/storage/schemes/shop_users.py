"""Схема таблицы для регистрации пользователей."""

from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy import sql

from backend.storage.schemes.config import Base


class ShopUsersScheme(Base):
    """Схема таблицы для регистрации пользователей."""
    __tablename__ = 'shopUsers'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), unique=False, nullable=False)
    isAdmin = Column(Boolean, unique=False, nullable=False, server_default=sql.expression.false())
