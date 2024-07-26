import faker
import pytest

from core.src.models import Hotel

faker = faker.Faker()


@pytest.fixture
def expected_hotel() -> dict:
   return {
        "hotel_id": faker.random_int(),
        "hotel_name": faker.word(),
        "hotel_price": faker.random_int(),
        "hotel_address": faker.word(),
        "hotel_rating": faker.random_int(1, 5),
        "amenities": [faker.random_int(), faker.random_int()],
        "hotel_city": faker.word(),
        "hotel_image": faker.word(),
        "hotel_country": faker.word(),
    }
    
