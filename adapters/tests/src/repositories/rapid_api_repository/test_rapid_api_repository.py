from typing import Callable

import pytest
from pytest_mock import MockerFixture

from core.src.exceptions import (HotelRepositoryException,
                                 RapidApiRepositoryException)


@pytest.mark.asyncio
async def test__rapid_api_repository_list_all_hotel_returns_hotels_when_succesful_connection(
    set_up_rapid_api_instance: Callable, expected_hotel
):
    rapid_api_repository = set_up_rapid_api_instance()
    
    hotel = await rapid_api_repository.list_all()
    single_hotel = hotel[0] 
    
    assert set(expected_hotel.keys()) == set(single_hotel.keys())
    

@pytest.mark.asyncio
async def test__rapid_api_repository_list_all_throws_exception_on_failure(
    set_up_rapid_api_instance: Callable,
    mocker: MockerFixture,
):
    expected_exception_message = "Exception while executing List All in Hotel"
    mocker.patch(
        "adapters.src.repositories.rapid_api.rapid_api_repository.RapidApiRepository.list_all",
        side_effect=HotelRepositoryException(method="List All"),
    )
    rapid_api_repository = set_up_rapid_api_instance()

    with pytest.raises(HotelRepositoryException) as captured_exception:
        await rapid_api_repository.list_all()

    assert str(captured_exception.value) == expected_exception_message


@pytest.mark.asyncio
async def test__rapid_api_repository_list_all_throws_exception_on_rapid_api_failure(
    set_up_rapid_api_instance: Callable,
    mocker: MockerFixture,
):
    mock_response = mocker.Mock()
    mock_response.status_code = 400
    mock_response.text = "Rapid API failed to get hotels"

    exception_to_raise = RapidApiRepositoryException(
        service_error_code=mock_response.status_code,
        service_error_message={"message": mock_response.text},
    )

    mocker.patch(
        "adapters.src.repositories.rapid_api.rapid_api_repository.RapidApiRepository.list_all",
        side_effect=exception_to_raise,
    )

    rapid_api_repository = set_up_rapid_api_instance()

    with pytest.raises(RapidApiRepositoryException) as captured_exception:
        await rapid_api_repository.list_all()

    assert captured_exception.value.service_error_code == 400
    assert (
        captured_exception.value.service_error_message
        == exception_to_raise.service_error_message
    )
