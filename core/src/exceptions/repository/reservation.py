from .base import RepositoryException


class ReservationRepositoryException(RepositoryException):
    def __init__(self, method: str):
        super().__init__(entity_type="Reservation", method=method)