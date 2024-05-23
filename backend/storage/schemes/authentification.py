"""Схема таблицы для регистрации пользователей."""

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class ShopUsersScheme(Base):
    """Схема таблицы для регистрации пользователей."""
    __tablename__ = 'shopUsers'

    idUser = Column(Integer, primary_key=True)
    nameUser = Column(String(50), unique=True, nullable=False)
    mailUser = Column(String(50), unique=True, nullable=False)
    passwordUser = Column(String(50), unique=False, nullable=False)
