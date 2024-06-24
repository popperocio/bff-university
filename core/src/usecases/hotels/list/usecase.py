from core.src.exceptions import (HotelBusinessException,
                                 HotelRepositoryException)
from core.src.repositories import HotelRepository

from .response import ListHotelResponse


class ListAll:
    def __init__(self, hotel_repository: HotelRepository):
        self.hotel_repository = hotel_repository

    async def execute(self):
        try:
            hotels_response = await self.hotel_repository.list_all()
            return ListHotelResponse(hotels=hotels_response)
        except HotelRepositoryException as error:
            raise HotelBusinessException(str(error))
