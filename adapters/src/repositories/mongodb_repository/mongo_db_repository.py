import datetime
from typing import Collection

from pymongo import MongoClient

from core.src import ReservationRequest
from core.src.exceptions import (ReservationConflictException,
                                 ReservationRepositoryException, ReservationBusinessException)
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
            checkin_date = datetime.datetime.strptime(reservation.checkin_date, '%a, %d %b %Y %H:%M:%S %Z')
            checkout_date = datetime.datetime.strptime(reservation.checkout_date, '%a, %d %b %Y %H:%M:%S %Z')
            overlapping_reservation = self.collection.find_one(
                {
                    "room_id": reservation.room_id,
                    "$and": [
                        {"checkin_date": {"$lt": checkout_date}},
                        {"checkout_date": {"$gt": checkin_date}}
                    ]
                }
            )
            if overlapping_reservation:
                raise ReservationConflictException(
                    "Room already booked for the given dates"
                )
            response = self.collection.insert_one(reservation.dict())
            reservation_id = str(response.inserted_id)
            return reservation_id
        except ReservationRepositoryException:
            raise ReservationBusinessException("Create Reservation")