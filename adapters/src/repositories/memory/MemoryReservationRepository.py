from typing import List

from core.src.models import Reservation
from core.src.usecases.reservations import ReservationRequest, ReservationResponse
from core.src.repositories import ReservationRepository

class MemoryReservationRepository(ReservationRepository):

    reservations: List[Reservation]
    current_id = str
    
    def __init__(self) -> None:
        self.reservations= []
        self.current_id="1"

    async def create_reservation(self, request: ReservationRequest) -> ReservationResponse:
        try:
            reservation_id = self.current_id
            self.current_id = str(int(self.current_id) + 1)
            new_reservation = Reservation(
                reservation_id=reservation_id,
                hotel_id=request.hotel_id,
                user_id=request.user_id,
                room_id=request.room_id,
                price=request.price,
                guest_name=request.guest_name,
                nights=request.nights,
                checkin_date=request.checkin_date,
                checkout_date=request.checkout_date,
                number_of_guests=request.number_of_guests,
            )
            self.reservations.append(new_reservation)
            return reservation_id
        except Exception as e:
            print("error memory", e)
