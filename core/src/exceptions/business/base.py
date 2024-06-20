class BusinessException(Exception):
  pass


class ExternalServiceException(BusinessException):
    """Base class for exceptions related with external services"""

    def __init__(
        self,
        message: str,
        service_error_code: int,
        service_error_message: str,
    ) -> None:
        """
        Args:
            message (str): A message to describe where the exception was raised
            service_error_code (int): Error code of the external service
            service_error_message (str): Error message of the external service
        """
        self.service_error_code = service_error_code
        self.service_error_message = service_error_message
        super().__init__(message)