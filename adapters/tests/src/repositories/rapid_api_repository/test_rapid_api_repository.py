import pytest

from core.src.exceptions import HotelRepositoryException


@pytest.mark.asyncio
async def test__rapid_api_repository_list_all_hotel_returns_hotels_when_succesful_connection(
    set_up_rapid_api_instance, expected_hotel
):
    rapid_api_repository = set_up_rapid_api_instance

    hotel = await rapid_api_repository.list_all()
    single_hotel = hotel[0]

    assert set(expected_hotel.keys()) == set(single_hotel.keys())


@pytest.mark.asyncio
async def test__rapid_api_repository_list_all_throws_exception_on_server_error(
    set_up_rapid_api_instance_server_error,
):
    rapid_api_repository = set_up_rapid_api_instance_server_error
    expected_message = "Exception while executing List All in Hotel"
    with pytest.raises(HotelRepositoryException) as captured_exception:
        await rapid_api_repository.list_all()

    assert str(captured_exception.value) == expected_message


@pytest.mark.asyncio
async def test__rapid_api_repository_list_all_throws_exception_on_bad_request(
    set_up_rapid_api_instance_400,
):
    rapid_api_repository = set_up_rapid_api_instance_400
    expected_message = "Exception while executing List All in Hotel"
    with pytest.raises(HotelRepositoryException) as captured_exception:
        await rapid_api_repository.list_all()

    assert str(captured_exception.value) == expected_message
