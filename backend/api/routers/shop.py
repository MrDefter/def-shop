"""Работа с магазином"""

from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse

from backend.api.service import PagesService


router_authentification = APIRouter(
    tags=['Работа с магазином'],
    prefix='/shop',
)