from core.src import ReservationRepository
from core.src.usecases.reservations import CreateReservation

from ..config.repositories import ReservationRepositoryConfig


def get_reservation_repository() -> ReservationRepository:
    return ReservationRepositoryConfig.get_repository()


def create_reservation_use_case() -> CreateReservation:
    return CreateReservation(reservation_repository=get_reservation_repository())
