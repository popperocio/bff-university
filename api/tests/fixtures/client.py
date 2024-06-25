import os
from typing import Callable

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from api.routers import hotels, reservations


@pytest.fixture
def environment_variables():
    os.environ["RAPID_API_URL"] = "RAPID_API_URL"
    os.environ["RAPID_API_HOST"] = "RAPID_API_HOST"
    os.environ["RAPID_API_KEY"] = "RAPID_API_KEY"
    os.environ["MONGO_DB_URL"] = "MONGO_DB_URL"
    os.environ["MONGO_DB_DATABASE"] = "MONGO_DB_DATABASE"
    os.environ["MONGO_DB_COLLECTION"] = "MONGO_DB_COLLECTION"


@pytest.fixture
def mock_fastapi_app(environment_variables) -> Callable:
    def _fixture() -> FastAPI:
        app = FastAPI()
        app.include_router(hotels.router, prefix="/hotels")
        app.include_router(reservations.router, prefix="/reservation")
        return app

    return _fixture


@pytest.fixture
def client() -> Callable:
    def _fixture(app: FastAPI):
        return TestClient(app)

    return _fixture
