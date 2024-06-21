from adapters.src.repositories import MemoryHotelRepository, RapidApiRepository
from core.src.repositories import HotelRepository
from core.src.utils import RestClient
from factories.config.rapid_api_hotels import HotelRapidAPI

memory_repository = MemoryHotelRepository()


def memory_hotel_repository() -> HotelRepository:
    return memory_repository


def rapid_api_repository() -> HotelRepository:
    return RapidApiRepository(
        client=RestClient,
        rapid_api_url=HotelRapidAPI.RAPID_API_URL,
        rapid_api_key=HotelRapidAPI.RAPID_API_KEY,
        rapid_api_host=HotelRapidAPI.RAPID_API_HOST,
    )
