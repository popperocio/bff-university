from typing import Callable

from pytest import fixture

from adapters.src.repositories import MongoDBReservationRepository
from factories.repositories import mongo_db_repository


@fixture
def set_up_mongo_db_instance() -> Callable:
    def _factory() -> MongoDBReservationRepository:
        return mongo_db_repository()

    return _factory
