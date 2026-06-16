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
def create(
    data: EstoqueCreate,
    db: Session = Depends(get_db),
):
    return EstoqueService.create(
        db,
        data,
    )


@router.get("/")
def list_all(
    db: Session = Depends(get_db),
):
    return EstoqueService.list_all(
        db,
    )
