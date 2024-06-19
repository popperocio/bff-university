from factories.repositories import memory_hotel_repository, rapid_api_repository
from .base import RepositoryConfig


class HotelRepositoryConfig(RepositoryConfig):
    _AVAILABLE_REPOSITORIES: list[str] = ["MEMORY", "RAPIDAPIREPOSITORY"]

    @classmethod
    def _get_repository_instances(cls) -> dict:
        return {
            "MEMORY": memory_hotel_repository(),
            "RAPIDAPIREPOSITORY": rapid_api_repository()
        }
