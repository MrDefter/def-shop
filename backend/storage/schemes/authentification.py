"""Схема таблицы для регистрации пользователей."""

from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import sql

Base = declarative_base()


class ShopUsersScheme(Base):
    """Схема таблицы для регистрации пользователей."""
    __tablename__ = 'shopUsers'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), unique=False, nullable=False)
    isAdmin = Column(Boolean, unique=False, nullable=False, server_default=sql.expression.false())
