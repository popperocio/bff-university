import os

from factories.repositories import (memory_reservation_repository,
                                    mongo_db_repository)

from .base import RepositoryConfig


class ReservationRepositoryConfig(RepositoryConfig):
    _REPOSITORY: str = os.getenv(
        "MEMORY_RESERVATION_REPOSITORY", "MONGODBRESERVATIONREPOSITORY"
    )
    _AVAILABLE_REPOSITORIES: list[str] = [
        "MEMORY_RESERVATION_REPOSITORY",
        "MONGODBRESERVATIONREPOSITORY",
    ]

    @classmethod
    def _get_repository_instances(cls) -> dict:
        return {
            "MEMORY_RESERVATION_REPOSITORY": memory_reservation_repository(),
            "MONGODBRESERVATIONREPOSITORY": mongo_db_repository(),
        }
