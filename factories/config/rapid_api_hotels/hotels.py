from ..utils import parse_env_variable


class HotelRapidAPI:
    RAPID_API_URL: str = parse_env_variable("RAPID_API_URL")
    RAPID_API_HOST = parse_env_variable("RAPID_API_HOST")
    RAPID_API_KEY = parse_env_variable("RAPID_API_KEY")
