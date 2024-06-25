from typing import Callable

import pytest
from core.src.exceptions import ReservationRepositoryException, ReservationConflictException
from pytest_mock import MockerFixture


@pytest.mark.asyncio
async def test__mongo_db_reservation_repository_returns_reservation_id_when_successful_creation(
    set_up_mongo_db_instance: Callable, mocker: MockerFixture, reservation_factory: Callable
):
    mocker.patch(
        "adapters.src.repositories.mongodb_repository.mongo_db_repository.MongoDBReservationRepository.create_reservation",
        return_value="1",
    )
    mongo_db_repository = set_up_mongo_db_instance()
    reservation= reservation_factory()
    expected_response = "1"
    
    response = await mongo_db_repository.create_reservation(reservation)

    assert response == expected_response
    
@pytest.mark.asyncio
async def test__mongo_db_repository_create_reservation_throws_exception_on_failure(
    set_up_mongo_db_instance: Callable, mocker: MockerFixture, reservation_factory: Callable
):
    expected_exception_message = "Exception while executing Create Reservation in Reservation"
    mocker.patch(
        "adapters.src.repositories.mongodb_repository.mongo_db_repository.MongoDBReservationRepository.create_reservation",
        side_effect=ReservationRepositoryException(method="Create Reservation"),
    )
    mongo_db_repository = set_up_mongo_db_instance()
    reservation= reservation_factory()
   
    with pytest.raises(ReservationRepositoryException) as captured_exception:
        await mongo_db_repository.create_reservation(reservation)

    assert str(captured_exception.value) == expected_exception_message


@pytest.mark.asyncio
async def test_mongo_db_reservation_repository_conflict_handling(
    set_up_mongo_db_instance: Callable, mocker: MockerFixture, reservation_factory: Callable
):
    mongo_db_repository = set_up_mongo_db_instance()
    reservation= reservation_factory()
    expected_exception_message = "Room already booked for the given dates"
    
    mocker.patch(
        "adapters.src.repositories.mongodb_repository.mongo_db_repository.MongoDBReservationRepository.create_reservation",
        side_effect=ReservationConflictException(message="Room already booked for the given dates"),
    )

    with pytest.raises(ReservationConflictException) as exc_info:
        await mongo_db_repository.create_reservation(reservation)

    assert str(exc_info.value) == expected_exception_message
