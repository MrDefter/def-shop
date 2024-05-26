"""Работа с базами данных."""

from .database import insert_user, insert_product, get_product, check_user, check_admin

__all__ = ['insert_user', 'insert_product', 'get_product', 'check_user', 'check_admin']
