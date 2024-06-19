from typing import Callable

import pytest
from pytest_mock import MockerFixture

from core.src.models import Hotel

@pytest.mark.asyncio
async def test__rapid_api_repository_list_all_hotel_returns_hotels_when_succesful_connection(
    set_up_rapid_api_instance: Callable,
    mocker: MockerFixture,
    expected_hotel
):
    mocker.patch(
        "adapters.src.repositories.rapid_api.rapid_api_repository.RapidApiRepository.list_all",
        return_value=expected_hotel,
    )
    rapid_api_repository = set_up_rapid_api_instance()
    hotel= await rapid_api_repository.list_all()
    
    assert expected_hotel == hotel
