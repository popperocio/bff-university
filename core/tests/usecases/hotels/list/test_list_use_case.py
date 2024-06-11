from typing import Callable

from adapters.src.repositories import MemoryHotelRepository
from core.src import HotelRepository, ListAll, ListHotelResponse

class TestListHotel:
    def test_should_return_a_list_of_hotels_response_when_reponse_is_successful(
        self, hotel_factory: Callable
    ) -> None:
        hotel_repository: HotelRepository = MemoryHotelRepository()
        hotel = hotel_factory
        hotel_repository.hotels.append(hotel)
        list_hotel_use_case = ListAll(hotel_repository)
        response = list_hotel_use_case.execute()
        expected_response = ListHotelResponse([hotel])
        assert response == expected_response
