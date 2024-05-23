"""Схема таблицы для регистрации пользователей."""

from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class RegistrationUserScheme(Base):
    """Схема таблицы для регистрации пользователей."""
    __tablename__ = 'shopUsers'

    nameUser = Column(String(50), nullable=False, unique=True)
    mailUser = Column(String(50), nullable=False, unique=True)
    passwordUser = Column(String(50), nullable=False, unique=False)
