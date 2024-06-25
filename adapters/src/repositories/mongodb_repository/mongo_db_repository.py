from typing import Collection, List
from core.src import ReservationRequest
from core.src.exceptions import ReservationRepositoryException,ReservationConflictException
from pymongo import MongoClient
from core.src.repositories import ReservationRepository

class MongoDBReservationRepository(ReservationRepository):
    def __init__(self, mongodb_url: str, db_name: str, collection_name: str) -> None:
        self.client: MongoClient = MongoClient(mongodb_url)
        self.db = self.client[db_name]
        self.collection: Collection = self.db[collection_name]
        self.collection.create_index([('room_id', 1), ('start_date', 1), ('end_date', 1)], unique=True)

    async def create_reservation(self, reservation:  ReservationRequest):
        try:
            existing_reservation = self.collection.find_one({
                'room_id': reservation.room_id,
                'checkin_date': {'$lte': reservation.checkin_date},
                'checkout_date': {'$gte': reservation.checkout_date}
            })
            if existing_reservation:
                raise ReservationConflictException("Room already booked for the given dates")
            response = self.collection.insert_one(reservation.dict())
            reservation_id = str(response.inserted_id) 
            return reservation_id
        except Exception as e:
            raise ReservationRepositoryException("Create Reservation")