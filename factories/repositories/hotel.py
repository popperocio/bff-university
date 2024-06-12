from adapters.src.repositories import MemoryHotelRepository
from core.src.repositories import HotelRepository


memory_repository = MemoryHotelRepository()

def memory_hotel_repository() -> HotelRepository:
    return memory_repository

