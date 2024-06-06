from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from .events.register import register_routers
from .routers import version


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(version)

    register_routers(app, "api.routers")
    return app
