from typing import List

from core.src.exceptions import HotelRepositoryException
from core.src.models import Hotel
from core.src.repositories import HotelRepository

class MemoryHotelRepository(HotelRepository):
    hotels: List[Hotel]

    def __init__(self) -> None:
        self.hotels = []

    async def list_all(self) -> List[Hotel]:
        try:
            return self.hotels
        except Exception:
           raise HotelRepositoryException("List All")