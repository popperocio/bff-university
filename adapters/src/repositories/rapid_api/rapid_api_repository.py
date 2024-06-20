
import json
from core.src.exceptions import HotelRepositoryException, RapidApiRepositoryException
from core.src.repositories import HotelRepository
from core.src.utils import RestClient, HttpStatus
from core.src.helpers import ParseHotelsRapidApi

class RapidApiRepository(HotelRepository):
    def __init__(
        self,
        client: type[RestClient],
        rapid_api_url: str,
        rapid_api_key: str,
        rapid_api_host: str,
    ) -> None:
        self.client = client(
            base_url=rapid_api_url,
            default_headers={
                'x-rapidapi-key': rapid_api_key,
                'x-rapidapi-host': rapid_api_host
            },
        )

    async def list_all(self) -> dict:
        response = await self.client.get(endpoint="/v2/hotels/downloadHotels?limit=2&language=en-US")
        try:
            hotels = response.text
            if response.status_code != HttpStatus.OK:
                raise RapidApiRepositoryException(
                    service_error_code=response.status_code,
                    service_error_message=response.text,
                )
            hotels_json = json.loads(hotels)
            hotels_result = ParseHotelsRapidApi.parse_hotels(hotels_json)
            return hotels_result
        except Exception:
            raise HotelRepositoryException("List All")
