from core.src.exceptions import ExternalServiceException

from .base import RepositoryException


class HotelRepositoryException(RepositoryException):
    def __init__(self, method: str):
        super().__init__(entity_type="Hotel", method=method)


class RapidApiRepositoryException(ExternalServiceException):
    """Exception raised when Rapid API fails"""

    def __init__(self, service_error_code: int, service_error_message: dict) -> None:
        """
        Args:
            service_error_code (int): Error code returned by Rapid API
            service_error_message (dict): Error message returned by Rapid API
        """
        formatted_error_message = ", ".join(
            f"{key}: {value}" for key, value in service_error_message.items()
        )

        super().__init__(
            message="Rapid API failed to get hotels",
            service_error_code=service_error_code,
            service_error_message=formatted_error_message,
        )
