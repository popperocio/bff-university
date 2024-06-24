from typing import Callable

import pytest

from core.src.repositories import ReservationRepository
from core.src import CreateReservation, ReservationResponse
from factories.repositories import memory_reservation_repository



class TestCreateReservation:
    
    @pytest.mark.asyncio
    async def test_should_return_a_reservation_of_a_given_hotel_when_reponse_is_successful(
        self,
        reservation_factory: Callable,
    ) -> None:
        reservation_repository: ReservationRepository = memory_reservation_repository()
        reservation_request= reservation_factory()
        create_reservation_use_case = CreateReservation(reservation_repository)
        
        response = await create_reservation_use_case.execute(reservation_request)
        expected_response = ReservationResponse(
            reservation_id=response.reservation_id,
            hotel_id= reservation_request.hotel_id,
            user_id= reservation_request.user_id,
            room_id= reservation_request.room_id,
            guest_name=reservation_request.guest_name,
            nights=reservation_request.nights,
            checkin_date=reservation_request.checkin_date,
            checkout_date= reservation_request.checkout_date,
            number_of_guests=reservation_request.number_of_guests,
            price= reservation_request.price
    )
        
    
        assert response == expected_response
