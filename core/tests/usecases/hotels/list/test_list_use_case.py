from typing import Callable

import pytest

from core.src import HotelRepository, ListAll, ListHotelResponse
from core.src.exceptions import (HotelBusinessException,
                                 HotelRepositoryException)
from factories.repositories import memory_hotel_repository


class TestListHotel:
    @pytest.mark.asyncio
    async def test_should_return_empty_list_when_no_hotels_found(self) -> None:
        hotel_repository: HotelRepository = memory_hotel_repository()
        list_hotel_use_case = ListAll(hotel_repository)
        expected_response = ListHotelResponse([])

        response = await list_hotel_use_case.execute()

        assert response == expected_response

    @pytest.mark.asyncio
    async def test_should_return_a_list_of_hotels_response_when_reponse_is_successful(
        self, hotel_factory: Callable
    ) -> None:
        hotel_repository: HotelRepository = memory_hotel_repository()
        hotel = hotel_factory
        hotel_repository.hotels.append(hotel)
        list_hotel_use_case = ListAll(hotel_repository)
        expected_response = ListHotelResponse([hotel])

        response = await list_hotel_use_case.execute()

        assert response == expected_response

    @pytest.mark.asyncio
    async def test_should_raise_business_exception_when_there_is_an_error(self, mocker):
        hotel_repository = memory_hotel_repository()
        list_hotel_use_case = ListAll(hotel_repository)
        mocker.patch.object(
            hotel_repository,
            "list_all",
            side_effect=HotelRepositoryException("List All"),
        )

        with pytest.raises(HotelBusinessException) as captured_exception:
            await list_hotel_use_case.execute()

        assert (
            str(captured_exception.value)
            == "Exception while executing List All in Hotel"
        )
