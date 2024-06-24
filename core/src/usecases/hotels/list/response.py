from typing import List, NamedTuple

from core.src.models import Hotel


class ListHotelResponse(NamedTuple):
    hotels: List[Hotel]
