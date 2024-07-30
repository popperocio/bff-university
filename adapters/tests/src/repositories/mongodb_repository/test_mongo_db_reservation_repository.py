from typing import Callable

import pytest

from core.src.exceptions import (ReservationBusinessException,
                                 ReservationConflictException)
from core.src.usecases.reservations import ReservationRequest


@pytest.mark.asyncio
async def test__mongo_db_reservation_repository_returns_reservation_id_when_successful_creation(
    set_up_mongo_db_instance,
    reservation_factory: Callable,
):
    mongo_db_repository = set_up_mongo_db_instance
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
async def test__mongo_db_repository_create_reservation_throws_exception_when_guest_name_missing(
    reservation_factory: Callable, set_up_mongo_db_instance
):
    mongo_db_repository = set_up_mongo_db_instance
    reservation = reservation_factory()
    reservation_dict = reservation.dict()
    reservation_dict["guest_name"] = ""
    modified_reservation = ReservationRequest(**reservation_dict)
    expected_message = "Guest name and email are required"

    with pytest.raises(ReservationBusinessException) as captured_exception:
        await mongo_db_repository.create_reservation(modified_reservation)

    assert str(captured_exception.value) == expected_message


@pytest.mark.asyncio
async def test__mongo_db_repository_create_reservation_throws_exception_when_email_missing(
    reservation_factory: Callable, set_up_mongo_db_instance
):
    mongo_db_repository = set_up_mongo_db_instance
    reservation = reservation_factory()
    reservation_dict = reservation.dict()
    reservation_dict["email"] = ""
    modified_reservation = ReservationRequest(**reservation_dict)
    expected_message = "Guest name and email are required"

    with pytest.raises(ReservationBusinessException) as captured_exception:
        await mongo_db_repository.create_reservation(modified_reservation)

    assert str(captured_exception.value) == expected_message


@pytest.mark.asyncio
async def test__mongo_db_repository_create_reservation_throws_exception_when_wrong_date(
    reservation_factory: Callable, set_up_mongo_db_instance
):
    mongo_db_repository = set_up_mongo_db_instance
    reservation = reservation_factory()
    reservation_dict = reservation.dict()
    reservation_dict["checkin_date"] = "2025-08-15"
    reservation_dict["check_out_date"] = "2025-07-15"
    modified_reservation = ReservationRequest(**reservation_dict)
    expected_message = "Check in date must be before check out date"

    with pytest.raises(ReservationBusinessException) as captured_exception:
        await mongo_db_repository.create_reservation(modified_reservation)

    assert str(captured_exception.value) == expected_message


@pytest.mark.asyncio
async def test_mongo_db_reservation_throws_exception_when_conflicting_reservation(
    set_up_mongo_db_instance,
    reservation_factory: Callable,
):
    mongo_db_repository = set_up_mongo_db_instance
    reservation = reservation_factory()
    expected_exception_message = "Room already booked for the given dates"
    mongo_db_repository.collection.delete_many({})
    await mongo_db_repository.create_reservation(reservation)

    with pytest.raises(ReservationConflictException) as exc_info:
        await mongo_db_repository.create_reservation(reservation)

    assert str(exc_info.value) == expected_exception_message
