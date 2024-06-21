from .base import BusinessException


class HotelBusinessException(BusinessException):
    """Hotel Business exception"""


class NotFoundException(BusinessException):
    def __init__(self, type):
        message = f"The {type} was not found."
        super().__init__(message)
