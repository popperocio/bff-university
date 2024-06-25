from adapters.src.repositories import MemoryReservationRepository, MongoDBReservationRepository
from core.src.repositories import ReservationRepository
from core.src.utils import RestClient
from factories.config.mongo_db_reservation import ReservationMongoDB

memory_repository = MemoryReservationRepository()


def memory_reservation_repository() -> ReservationRepository:
    return memory_repository



def mongo_db_repository() -> ReservationRepository:
    return MongoDBReservationRepository(
        mongodb_url=ReservationMongoDB.MONGO_DB_URL,
        db_name= ReservationMongoDB.MONGO_DB_DATABASE,
        collection_name= ReservationMongoDB.MONGO_DB_COLLECTION
    )
