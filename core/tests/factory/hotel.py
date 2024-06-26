from typing import Any, Callable

import pytest
from faker import Faker

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
                    "hotel_rating": faker.random_int(1, 5),
                    "amenities": [faker.random_int],
                    "hotel_city": faker.word(),
                    "hotel_image": faker.word(),
                    "hotel_country": faker.word(),
                },
                **kwargs,
            }
        )

    return _factory
