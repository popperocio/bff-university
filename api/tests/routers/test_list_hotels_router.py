from http import HTTPStatus
from typing import Callable

from fastapi.testclient import TestClient
from pytest_mock import MockerFixture

from core.src.exceptions import (BusinessException, NotFoundException,
                                 RepositoryException)


def test_list_all_hotels_returns_200_status_code_when_hotels_are_retrieved_successfully(
    mocker: MockerFixture,
    mock_fastapi_app: Callable,
    client: TestClient,
    hotel_factory: Callable,
):
    app = mock_fastapi_app()
    client = TestClient(app)
    hotels = hotel_factory()
    mocker.patch(
        "core.src.usecases.hotels.list.usecase.ListAll.execute",
        return_value=hotels,
    )

    response = client.get(url="/hotels")

    assert response.status_code == 200


def test_list_all_hotels_returns_404_status_code_when_not_found(
    mocker: MockerFixture,
    mock_fastapi_app: Callable,
    client: TestClient,
):
    app = mock_fastapi_app()
    client = TestClient(app)
    expected_message = {"detail": "Not Found"}
    mocker.patch(
        "core.src.usecases.hotels.list.usecase.ListAll.execute",
        side_effect=NotFoundException("Hotels not found"),
    )
    response = client.get(url="/hotel")

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == expected_message


def test_list_all_hotels_returns_400_status_code_when_business_exception_occurs(
    mocker: MockerFixture,
    mock_fastapi_app: Callable,
    client: TestClient,
):
    app = mock_fastapi_app()
    client = TestClient(app)
    expected_message = {"detail": "Business logic error"}

    mocker.patch(
        "core.src.usecases.hotels.list.usecase.ListAll.execute",
        side_effect=BusinessException("Business logic error"),
    )

    response = client.get(url="/hotels")

    assert response.status_code == 400
    assert response.json() == expected_message


def test_list_all_hotels_returns_500_status_code_when_repository_exception_occurs(
    mocker: MockerFixture,
    mock_fastapi_app: Callable,
    client: TestClient,
):
    app = mock_fastapi_app()
    client = TestClient(app)
    expected_message = {"detail": "Exception while executing List All in Hotels"}

    mocker.patch(
        "core.src.usecases.hotels.list.usecase.ListAll.execute",
        side_effect=RepositoryException(entity_type="Hotels", method="List All"),
    )

    response = client.get(url="/hotels")

    assert response.status_code == 500
    assert response.json() == expected_message
