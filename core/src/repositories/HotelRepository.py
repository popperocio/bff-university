from abc import ABC, abstractmethod
from typing import List

from core.src.models import Hotel


class HotelRepository(ABC):

    @abstractmethod
    def list_all(self) -> List[Hotel]:
        raise NotImplementedError