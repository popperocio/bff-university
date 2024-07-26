from typing import Callable

import pytest
from pytest_mock import MockerFixture

from core.src.exceptions import (ReservationConflictException,
                                 ReservationRepositoryException)


@pytest.mark.asyncio
async def test__mongo_db_reservation_repository_returns_reservation_id_when_successful_creation(
    set_up_mongo_db_instance: Callable,
    reservation_factory: Callable,
):
    mongo_db_repository = set_up_mongo_db_instance()
    reservation = reservation_factory()

    response = await mongo_db_repository.create_reservation(reservation)
    
    assert response is not None
    assert response.hotel_id == reservation.hotel_id
    assert response.user_id == reservation.user_id
    assert response.room_id == reservation.room_id
    assert response.checkin_date == reservation.checkin_date
    assert response.checkout_date == reservation.checkout_date
    assert response.price == reservation.price
    assert response.guest_name == reservation.guest_name
    assert response.nights == reservation.nights
    assert response.number_of_guests == reservation.number_of_guests
    assert response.email == reservation.email


@pytest.mark.asyncio
async def test__mongo_db_repository_create_reservation_throws_exception_on_failure(
    set_up_mongo_db_instance: Callable,
    mocker: MockerFixture,
    reservation_factory: Callable,
):
    expected_exception_message = (
        "Exception while executing Create Reservation in Reservation"
    )
    mocker.patch(
        "adapters.src.repositories.mongodb_repository.mongo_db_repository.MongoDBReservationRepository.create_reservation",  # noqa
        side_effect=ReservationRepositoryException(method="Create Reservation"),
    )
    mongo_db_repository = set_up_mongo_db_instance()
    reservation = reservation_factory()

    with pytest.raises(ReservationRepositoryException) as captured_exception:
        await mongo_db_repository.create_reservation(reservation)

    assert str(captured_exception.value) == expected_exception_message


@pytest.mark.asyncio
async def test_mongo_db_reservation_repository_conflict_handling(
    set_up_mongo_db_instance: Callable,
    mocker: MockerFixture,
    reservation_factory: Callable,
):
    mongo_db_repository = set_up_mongo_db_instance()
    reservation = reservation_factory()
    expected_exception_message = "Room already booked for the given dates"

    mocker.patch(
        "adapters.src.repositories.mongodb_repository.mongo_db_repository.MongoDBReservationRepository.create_reservation",  # noqa
        side_effect=ReservationConflictException(
            message="Room already booked for the given dates"
        ),
    )

    with pytest.raises(ReservationConflictException) as exc_info:
        await mongo_db_repository.create_reservation(reservation)

    assert str(exc_info.value) == expected_exception_message
