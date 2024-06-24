from abc import ABC, abstractmethod

from ..usecases.reservations import ReservationResponse, ReservationRequest
class ReservationRepository(ABC):

    @abstractmethod
    def create_reservation(self, request: ReservationRequest) -> ReservationResponse:
        raise NotImplementedError
