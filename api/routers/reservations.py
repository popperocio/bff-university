from fastapi import APIRouter, Depends, HTTPException, status

from core.src.exceptions import BusinessException, RepositoryException
from core.src.usecases.reservations import (CreateReservation,
                                            ReservationRequest)
from factories.usecases.reservation import create_reservation_use_case

router = APIRouter(
    tags=["reservation"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)


@router.post("/")
async def create_reservation(
    request: ReservationRequest,
    create_reservation_use_case: CreateReservation = Depends(
        create_reservation_use_case
    ),
):
    try:
        create_reservation_response = await create_reservation_use_case.execute(request)
        return create_reservation_response
    except BusinessException as e:
        raise HTTPException(detail=e.__str__(), status_code=status.HTTP_400_BAD_REQUEST)
    except RepositoryException as e:
        raise HTTPException(
            detail=e.__str__(), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
