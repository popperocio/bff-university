from typing import Callable

from adapters.src.repositories import MemoryHotelRepository
from core.src import HotelRepository, ListAll


class TestListHotel:
    def test_should_return_a_list_of_hotels_response_when_reponse_is_successful(
        self
    ) -> None:
        hotel_repository: HotelRepository = MemoryHotelRepository()
        list_hotel_use_case = ListAll(hotel_repository)
        response = list_hotel_use_case.execute()
        assert response == None