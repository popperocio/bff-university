from datetime import date
from typing import NamedTuple, Optional


class Reservation(NamedTuple):
    reservation_id: int
    hotel_id: int
    user_id: int
    room_id: int
    price: Optional[float]
    guest_name: str
    nights: int
    checkin_date: date
    checkout_date: date
    number_of_guests: int
    email: str


class ReservationResponse(NamedTuple):
    reservation_id: str
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
