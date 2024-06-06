from typing import Any, Callable

from faker import Faker
from pytest import fixture

from core.src.models import Hotel


@fixture
def hotel_factory(
    faker: Faker,
) -> Callable:
    def _factory(**kwargs: Any) -> Hotel:
        return Hotel(
            **{
                **{
                    "hotel_id": faker.uuid4(),
                    "hotel_name": faker.word(),
                    "hotel_price": faker.int(),
                    "hotel_address": faker.word(),
                    "hotel_rating": faker.int(),
                },
                **kwargs,
            }
        )

    return _factory