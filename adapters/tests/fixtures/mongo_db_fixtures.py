import os
from pytest import fixture

from adapters.src.repositories import MongoDBReservationRepository

@fixture
def set_up_mongo_db_instance() -> MongoDBReservationRepository:
    host = os.getenv("MONGO_DB_HOST", "localhost")
    port = int(os.getenv("MONGO_DB_PORT", 27017))
    database_name = os.getenv("MONGODB_DB_NAME", "mongodb")
    collection_name = os.getenv("MONGODB_COLLECTION_NAME", "reservation")
    uri = f"mongodb://{host}:{port}/{database_name}"

    return MongoDBReservationRepository(
        mongodb_url=uri, db_name=database_name, collection_name=collection_name
    )