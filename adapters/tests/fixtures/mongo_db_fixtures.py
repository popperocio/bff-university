from pytest import fixture

from adapters.src.repositories import MongoDBReservationRepository

@fixture
def set_up_mongo_db_instance() -> MongoDBReservationRepository:
    host = "mongodb"
    port = 27017
    database_name = "mongodb"
    uri = f"mongodb://{host}:{port}/{database_name}"

    return MongoDBReservationRepository(
        mongodb_url=uri, db_name=database_name, collection_name="reservation"
    )
