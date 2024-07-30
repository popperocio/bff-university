from typing import Callable

from pytest import fixture
from pytest_mock_resources import create_mongo_fixture

from adapters.src.repositories import MongoDBReservationRepository


mongo = create_mongo_fixture()

@fixture
def set_up_mongo_db_instance(mongo) -> MongoDBReservationRepository:
    host = mongo.pmr_credentials.host
    port = mongo.pmr_credentials.port
    database_name = mongo.pmr_credentials.database
    uri = f"mongodb://{host}:{port}/{database_name}"

    return MongoDBReservationRepository(
        mongodb_url=uri,
        db_name=database_name,
        collection_name="reservation"
    )