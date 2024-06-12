from core.src.exceptions import HotelRepositoryException, HotelBusinessException
from core.src.repositories import HotelRepository
from .response import ListHotelResponse

class ListAll:
    def __init__(self, hotel_repository: HotelRepository):
        self.hotel_repository = hotel_repository

    def execute(self):
        try:
            repository_hotel = self.hotel_repository.list_all()
            return ListHotelResponse(hotels=repository_hotel)
        except HotelRepositoryException as error:
            raise HotelBusinessException(str(error))