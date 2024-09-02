"""Роутеры."""

from .admin import router_admin
from .pages import router_pages
from .authentification import router_authentification
from .shop import router_shop


__all__ = ['router_admin', 'router_pages', 'router_authentification', 'router_shop']
