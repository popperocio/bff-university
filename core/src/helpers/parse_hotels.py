from typing import List

from core.src.models import Hotel


class ParseHotelsRapidApi:
    def __init__(self) -> None:
        pass

    @classmethod
    def parse_hotels(self, hotels_response: list) -> List[Hotel]:
        hotels_data = hotels_response["getSharedBOF2.Downloads.Hotel.Hotels"][
            "results"
        ]["hotels"]
        hotels_result = []
        for hotel_id, hotel_info in hotels_data.items():
            hotel = {
                "hotel_id": int(hotel_info["hotelid_ppn"]),
                "hotel_name": hotel_info.get("hotel_name"),
                "hotel_price": (
                    None
                    if hotel_info.get("review_count") == "0"
                    else float(hotel_info.get("review_count"))
                ),
                "hotel_address": hotel_info.get("hotel_address"),
                "hotel_rating": (
                    float(hotel_info.get("star_rating"))
                    if hotel_info.get("star_rating")
                    else None
                ),
                "amenities": hotel_info.get("amenity_codes"),
            }
            hotels_result.append(hotel)
        return hotels_result
