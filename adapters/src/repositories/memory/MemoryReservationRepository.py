from typing import List

from core.src.exceptions import (ReservationConflictException,
                                 ReservationRepositoryException)
from core.src.exceptions.business.reservation import ReservationBusinessException
from core.src.models import Reservation
from core.src.repositories import ReservationRepository
from core.src.usecases.reservations import (ReservationRequest,
                                            ReservationResponse)


class MemoryReservationRepository(ReservationRepository):

    reservations: List[Reservation]
    current_id = str

    def __init__(self) -> None:
        self.reservations = []
        self.current_id = "1"

    async def create_reservation(
        self, request: ReservationRequest
    ) -> ReservationResponse:
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
                email=request.email
            )
            if self._has_conflict(new_reservation):
                raise ReservationConflictException(
                    "Room already booked for the given dates"
                )

            self.reservations.append(new_reservation)
            return reservation_id
        except ReservationRepositoryException:
            ReservationBusinessException("Create Reservation")

    def _has_conflict(self, new_reservation: Reservation) -> bool:
        """Check if there is a conflict with existing reservations."""
        for existing_reservation in self.reservations:
            if (
                existing_reservation.room_id == new_reservation.room_id
                and existing_reservation.checkin_date <= new_reservation.checkout_date
                and existing_reservation.checkout_date >= new_reservation.checkin_date
            ):
                return True
        return False
