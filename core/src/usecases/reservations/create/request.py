from typing import Optional

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
    email: str
