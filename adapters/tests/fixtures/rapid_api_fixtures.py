from typing import Callable

from pytest import fixture

from adapters.src.repositories import RapidApiRepository
from factories.repositories import rapid_api_repository


@fixture
def set_up_rapid_api_instance() -> Callable:
    def _factory() -> RapidApiRepository:
        return rapid_api_repository()
    return _factory