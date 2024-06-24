from typing import NamedTuple, Optional
from datetime import date
from pydantic import BaseModel

class ReservationRequest(BaseModel):
    hotel_id: int
    user_id: int
    room_id: int
    guest_name: str
    nights: int
    checkin_date: str
    checkout_date: str
    number_of_guests: int
    price: Optional[float]

