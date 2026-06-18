from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.estoque import (
    EstoqueCreate,
    EstoqueResponse,
)
from app.services.estoque_service import (
    EstoqueService,
)

router = APIRouter(
    prefix="/estoque",
    tags=["Estoque"],
)


@router.post(
    "/",
    response_model=EstoqueResponse,
    status_code=HTTPStatus.CREATED,
)
def create_estoque(
    data: EstoqueCreate,
    db: Session = Depends(get_db),
):
    return EstoqueService.create(
        db,
        data,
    )


@router.get(
    "/",
    response_model=list[EstoqueResponse],
)
def list_estoque(
    db: Session = Depends(get_db),
):
    return EstoqueService.list_all(
        db,
    )


@router.get(
    "/{estoque_id}",
    response_model=EstoqueResponse,
)
def get_estoque(
    estoque_id: int,
    db: Session = Depends(get_db),
):
    return EstoqueService.get_by_id(
        db,
        estoque_id,
    )
