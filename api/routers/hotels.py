from fastapi import APIRouter, Depends, HTTPException, status

from core.src.exceptions import (BusinessException, NotFoundException,
                                 RepositoryException)
from core.src.usecases.hotels import ListAll
from factories.usecases.hotel import list_hotel_use_case

router = APIRouter(
    tags=["hotels"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)


@router.get("/")
async def list_all_hotels(
    hotels_use_case: ListAll = Depends(list_hotel_use_case),
):
    try:
        list_hotels_response = await hotels_use_case.execute()
        if not list_hotels_response:
            raise NotFoundException("Hotels not found")
        return list_hotels_response
    except BusinessException as e:
        raise HTTPException(detail=e.__str__(), status_code=status.HTTP_400_BAD_REQUEST)
    except RepositoryException as e:
        raise HTTPException(
            detail=e.__str__(), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
