from typing import NamedTuple, Optional


class Hotel(NamedTuple):
    hotel_id: int
    hotel_name: Optional[str]
    hotel_price: Optional[float]
    hotel_address: Optional[str]
    hotel_rating: Optional[float]
