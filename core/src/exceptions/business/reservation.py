from .base import BusinessException


class ReservationBusinessException(BusinessException):
    """Reservation Business exception"""


class ReservationConflictException(ReservationBusinessException):
    """Exception raised when a reservation conflicts with existing bookings."""

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)
