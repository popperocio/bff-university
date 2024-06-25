from typing import Callable

import pytest
from pytest_mock import MockerFixture


@pytest.mark.asyncio
async def test__mongo_db_reservation_repository_returns_reservation_id_when_successful_creation(
    set_up_mongo_db_instance: Callable, mocker: MockerFixture, reservation_factory: Callable
):
    mocker.patch(
        "adapters.src.repositories.mongodb_repository.mongo_db_repository.MongoDBReservationRepository.create_reservation",
        return_value="1",
    )
    mongo_db_repository = set_up_mongo_db_instance()
    reservation= reservation_factory()
    expected_response = "1"
    
    response = await mongo_db_repository.create_reservation(reservation)

    assert response == expected_response
