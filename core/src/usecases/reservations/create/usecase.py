from core.src.repositories import ReservationRepository
from .response import ReservationResponse
from .request import ReservationRequest


class CreateReservation:
    def __init__(self, reservation_repository: ReservationRepository):
        self.reservation_repository = reservation_repository

    async def execute(self, request: ReservationRequest):
        try:
            reservation_response = await self.reservation_repository.create_reservation(request)
            return ReservationResponse(
                    reservation_id=reservation_response,
                    hotel_id= request.hotel_id,
                    user_id= request.user_id,
                    room_id= request.room_id,
                    guest_name=request.guest_name,
                    nights=request.nights,
                    checkin_date=request.checkin_date,
                    checkout_date= request.checkout_date,
                    number_of_guests=request.number_of_guests,
                    price= request.price
            )
        except Exception as error:
            print(error)
            pass
