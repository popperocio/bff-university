from http import HTTPStatus
import json
from typing import Callable

from core.src import ReservationResponse, ReservationRequest
from fastapi.testclient import TestClient
from pytest_mock import MockerFixture



def test_create_reservation_returns_200_status_code_when_reservation_is_stored_successfully(
    mocker: MockerFixture,
    mock_fastapi_app: Callable,
    client: TestClient,
    reservation_factory: Callable
):
    app = mock_fastapi_app()
    client = TestClient(app)
    request= reservation_factory()
    expected_response = ReservationResponse(
                    reservation_id="1",
                    hotel_id= request.hotel_id,
                    user_id= request.user_id,
                    room_id= request.room_id,
                    guest_name= request.guest_name,
                    nights= request.nights,
                    checkin_date=request.checkin_date,
                    checkout_date= request.checkout_date,
                    number_of_guests=request.number_of_guests,
                    price= request.price
            )
    data = request.dict()
    json_data = json.dumps(data)

    mocker.patch(
        "core.src.usecases.reservations.create.usecase.CreateReservation.execute",
        return_value=expected_response,
    )
    response = client.post("/reservation/", data=json_data)

    assert response.status_code == 200
    