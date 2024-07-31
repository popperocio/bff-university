import json
from typing import Callable

from fastapi.testclient import TestClient
from adapters.src.repositories import MemoryReservationRepository
from pytest_mock import MockerFixture
import mongomock
from core.src import ReservationResponse
from core.src.exceptions import BusinessException, RepositoryException


def test_create_reservation_returns_200_status_code_when_reservation_is_stored_successfully(
    mocker: MockerFixture,
    mock_fastapi_app: Callable,
    client: TestClient,
    reservation_factory: Callable,
):
    mock_db = mongomock.MongoClient().db
    mocker.patch(
        'adapters.src.repositories.memory.MemoryReservationRepository',
        new=mocker.MagicMock(
            collection=mock_db.reservations
        )
    )
    mocker.patch(
        'factories.config.repositories.reservation.ReservationRepositoryConfig.get_repository',
        return_value=MemoryReservationRepository()
    )
    app = mock_fastapi_app()
    client = TestClient(app)
    request = reservation_factory()
    data = request.model_dump()
    json_data = json.dumps(data)
    expected_response = ReservationResponse(
        reservation_id="1",
        hotel_id=request.hotel_id,
        user_id=request.user_id,
        room_id=request.room_id,
        guest_name=request.guest_name,
        nights=request.nights,
        checkin_date=request.checkin_date,
        checkout_date=request.checkout_date,
        number_of_guests=request.number_of_guests,
        price=request.price,
        email=request.email,
    )

    mocker.patch(
        "core.src.usecases.reservations.create.usecase.CreateReservation.execute",
        return_value=expected_response,
    )
    response = client.post("/reservation/", content=json_data)

    assert response.status_code == 200


def test_create_reservation_returns_400_status_code_when_business_exception_occurs(
    mocker: MockerFixture,
    mock_fastapi_app: Callable,
    client: TestClient,
    reservation_factory: Callable,
):
    mock_db = mongomock.MongoClient().db
    mocker.patch(
        'adapters.src.repositories.memory.MemoryReservationRepository',
        new=mocker.MagicMock(
            collection=mock_db.reservations
        )
    )
    mocker.patch(
        'factories.config.repositories.reservation.ReservationRepositoryConfig.get_repository',
        return_value=MemoryReservationRepository()
    )
    app = mock_fastapi_app()
    client = TestClient(app)
    request = reservation_factory()
    data = request.model_dump()
    json_data = json.dumps(data)
    expected_message = {"detail": "Business logic error"}

    mocker.patch(
        "core.src.usecases.reservations.create.usecase.CreateReservation.execute",
        side_effect=BusinessException("Business logic error"),
    )

    response = client.post(url="/reservation/", content=json_data)

    assert response.status_code == 400
    assert response.json() == expected_message


def test_create_reservation_returns_500_status_code_when_repository_exception_occurs(
    mocker: MockerFixture,
    mock_fastapi_app: Callable,
    client: TestClient,
    reservation_factory: Callable,
):
    mock_db = mongomock.MongoClient().db
    mocker.patch(
        'adapters.src.repositories.memory.MemoryReservationRepository',
        new=mocker.MagicMock(
            collection=mock_db.reservations
        )
    )
    mocker.patch(
        'factories.config.repositories.reservation.ReservationRepositoryConfig.get_repository',
        return_value=MemoryReservationRepository()
    )
    app = mock_fastapi_app()
    client = TestClient(app)
    request = reservation_factory()
    data = request.model_dump()
    json_data = json.dumps(data)
    expected_message = {
        "detail": "Exception while executing Create Reservation in Reservation"
    }

    mocker.patch(
        "core.src.usecases.reservations.create.usecase.CreateReservation.execute",
        side_effect=RepositoryException(
            entity_type="Reservation", method="Create Reservation"
        ),
    )

    response = client.post(url="/reservation/", content=json_data)

    assert response.status_code == 500
    assert response.json() == expected_message
