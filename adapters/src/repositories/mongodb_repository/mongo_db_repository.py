from typing import Collection

from dateutil import parser
from pymongo import MongoClient

from core.src import ReservationRequest
from core.src.exceptions import (ReservationBusinessException,
                                 ReservationConflictException,
                                 ReservationRepositoryException)
from core.src.models import ReservationResponse
from core.src.repositories import ReservationRepository


class MongoDBReservationRepository(ReservationRepository):
    def __init__(self, mongodb_url: str, db_name: str, collection_name: str) -> None:
        self.client: MongoClient = MongoClient(mongodb_url)
        self.db = self.client[db_name]
        self.collection: Collection = self.db[collection_name]
        self.collection.create_index(
            [("room_id", 1), ("checkin_date", 1), ("checkout_date", 1)], unique=True
        )

    async def create_reservation(self, reservation: ReservationRequest):
        try:
            checkin_date = parser.parse(reservation.checkin_date)
            checkout_date = parser.parse(reservation.checkout_date)
            overlapping_reservation = self.collection.find_one(
                {
                    "room_id": reservation.room_id,
                    "$and": [
                        {"checkin_date": {"$lt": checkout_date}},
                        {"checkout_date": {"$gt": checkin_date}},
                    ],
                }
            )
            if overlapping_reservation:
                raise ReservationConflictException(
                    "Room already booked for the given dates"
                )
            response = self.collection.insert_one(reservation.model_dump())
            reservation_id = str(response.inserted_id)
            return ReservationResponse(
                reservation_id=reservation_id,
                hotel_id=reservation.hotel_id,
                user_id=reservation.user_id,
                room_id=reservation.room_id,
                price=reservation.price,
                guest_name=reservation.guest_name,
                nights=reservation.nights,
                checkin_date=reservation.checkin_date,
                checkout_date=reservation.checkout_date,
                number_of_guests=reservation.number_of_guests,
                email=reservation.email,
            )
        except ReservationRepositoryException:
            raise ReservationBusinessException("Create Reservation")
