from typing import Any, Callable

from faker import Faker
from pytest import fixture
import pytest

from core.src.models import Hotel


@pytest.fixture
def hotel_factory(
    faker: Faker,
) -> Callable:
    def _factory(**kwargs: Any) -> Hotel:
        return Hotel(
            **{
                **{
                    "hotel_id": faker.uuid4(),
                    "hotel_name": faker.word(),
                    "hotel_price": faker.random_int(),
                    "hotel_address": faker.word(),
                    "hotel_rating": faker.random_int(1,5),
                    "amenities": [faker.random_int]
                },
                **kwargs,
            }
        )

    return _factory