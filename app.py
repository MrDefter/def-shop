from fastapi import FastAPI

from backend.api.routers import router_admin, router_pages, router_authentification


def make_app() -> FastAPI:
    """Создание приложения.

    Returns:
        Приложение FastAPI.
    """
    app = FastAPI(
        docs_url='/',
        debug=True
    )
    app.include_router(router_admin)
    app.include_router(router_authentification)
    app.include_router(router_pages)

    return app
