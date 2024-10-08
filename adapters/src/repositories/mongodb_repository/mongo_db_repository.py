from typing import Collection

from dateutil import parser
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

from core.src import ReservationRequest
from core.src.exceptions import (ReservationBusinessException,
                                 ReservationConflictException,
                                 ReservationRepositoryException)
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
            if checkin_date >= checkout_date:
                raise ReservationBusinessException(
                    "Check in date must be before check out date"
                )
            if not reservation.guest_name or not reservation.email:
                raise ReservationBusinessException("Guest name and email are required")
            response = self.collection.insert_one(reservation.model_dump())
            reservation_id = str(response.inserted_id)
            return reservation_id
        except DuplicateKeyError:
            raise ReservationConflictException(
                "Room already booked for the given dates"
            )
        except ReservationRepositoryException:
            raise ReservationBusinessException("Create Reservation")
