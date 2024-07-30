from typing import Callable

import pytest

from core.src import CreateReservation, ReservationResponse
from core.src.exceptions import (ReservationBusinessException,
                                 ReservationConflictException,
                                 ReservationRepositoryException)
from core.src.repositories import ReservationRepository
from factories.repositories import memory_reservation_repository


class TestCreateReservation:
    @pytest.mark.asyncio
    async def test_should_return_a_reservation_of_a_given_hotel_when_reponse_is_successful(
        self,
        reservation_factory: Callable,
    ) -> None:
        reservation_repository: ReservationRepository = memory_reservation_repository()
        reservation_request = reservation_factory()
        create_reservation_use_case = CreateReservation(reservation_repository)

        response = await create_reservation_use_case.execute(reservation_request)
        expected_response = ReservationResponse(
            reservation_id=response.reservation_id,
            hotel_id=reservation_request.hotel_id,
            user_id=reservation_request.user_id,
            room_id=reservation_request.room_id,
            guest_name=reservation_request.guest_name,
            nights=reservation_request.nights,
            checkin_date=reservation_request.checkin_date,
            checkout_date=reservation_request.checkout_date,
            number_of_guests=reservation_request.number_of_guests,
            price=reservation_request.price,
            email=reservation_request.email,
        )

        assert response == expected_response

    @pytest.mark.asyncio
    async def test_should_raise_business_exception_when_there_is_an_error(
        self,
        mocker,
        reservation_factory: Callable,
    ):
        reservation_repository: ReservationRepository = memory_reservation_repository()
        reservation_request = reservation_factory()
        create_reservation_use_case = CreateReservation(reservation_repository)
        expected_message = "Exception while executing Create Reservation in Reservation"

        mocker.patch.object(
            reservation_repository,
            "create_reservation",
            side_effect=ReservationRepositoryException("Create Reservation"),
        )

        with pytest.raises(ReservationBusinessException) as captured_exception:
            await create_reservation_use_case.execute(reservation_request)

        assert str(captured_exception.value) == expected_message

    @pytest.mark.asyncio
    async def test_create_reservation_conflict(
        self,
        reservation_factory: Callable,
    ) -> None:
        reservation_repository: ReservationRepository = memory_reservation_repository()
        reservation_request = reservation_factory()
        create_reservation_use_case = CreateReservation(reservation_repository)
        expected_message = "Room already booked for the given dates"

        with pytest.raises(ReservationConflictException) as captured_exception:
            await create_reservation_use_case.execute(reservation_request)

        assert str(captured_exception.value) == expected_message
