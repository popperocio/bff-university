from core.src.repositories import HotelRepository

class ListAll:
    def __init__(self, hotel_repository: HotelRepository):
        self.hotel_repository = hotel_repository

    def execute(self):
        try:
            repository_hotel = self.hotel_repository.list_all()
            return repository_hotel
        except:
            pass