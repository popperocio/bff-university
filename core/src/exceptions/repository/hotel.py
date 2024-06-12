from .base import RepositoryException

class HotelRepositoryException(RepositoryException):
  def __init__(self, method: str):
    super().__init__(entity_type="Hotel", method=method)
