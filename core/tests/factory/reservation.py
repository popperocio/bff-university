from datetime import date, timedelta
from typing import Any, Callable

import pytest
from faker import Faker

from core.src import ReservationRequest


@pytest.fixture
def reservation_factory(
    faker: Faker,
) -> Callable:
    def _factory(**kwargs: Any) -> ReservationRequest:
        today = date.today()
        checkin_date = faker.date_between(
            start_date=today, end_date=today + timedelta(days=30)
        )
        checkout_date = faker.date_between(
            start_date=checkin_date + timedelta(days=1),
            end_date=checkin_date + timedelta(days=15),
        )

        return ReservationRequest(
            **{
                **{
                    "hotel_id": faker.random_int(min=1, max=1000),
                    "user_id": faker.random_int(min=1, max=1000),
                    "room_id": faker.random_int(min=1, max=1000),
                    "price": faker.random_int(min=50, max=500),
                    "guest_name": faker.name(),
                    "nights": (checkout_date - checkin_date).days,
                    "checkin_date": checkin_date.isoformat(),
                    "checkout_date": checkout_date.isoformat(),
                    "number_of_guests": faker.random_int(min=1, max=5),
                },
                **kwargs,
            }
        )

    return _factory
