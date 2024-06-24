from adapters.src.repositories import MemoryReservationRepository
from core.src.repositories import ReservationRepository
from core.src.utils import RestClient

memory_repository = MemoryReservationRepository()


def memory_reservation_repository() -> ReservationRepository:
    return memory_repository
