from core.src import HotelRepository
from core.src.usecases.hotels import ListAll

from ..config.repositories import HotelRepositoryConfig


def get_hotel_repository() -> HotelRepository:
    return HotelRepositoryConfig.get_repository()


def list_hotel_use_case() -> ListAll:
    return ListAll(hotel_repository=get_hotel_repository())
