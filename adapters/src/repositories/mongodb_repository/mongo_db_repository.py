from typing import Collection, List
from core.src import ReservationRequest
from pymongo import MongoClient

from core.src.repositories import ReservationRepository

class MongoDBReservationRepository(ReservationRepository):
    def __init__(self, mongodb_url: str, db_name: str, collection_name: str) -> None:
        self.client: MongoClient = MongoClient(mongodb_url)
        self.db = self.client[db_name]
        self.collection: Collection = self.db[collection_name]

    async def create_reservation(self, reservation:  ReservationRequest):
        try:
            response = self.collection.insert_one(reservation.dict())
            reservation_id = str(response.inserted_id) 
            return reservation_id
        except Exception as e:
            raise e