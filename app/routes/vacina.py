from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.vacina import (
    VacinaCreate,
    VacinaResponse,
)
from app.services.vacina_service import (
    VacinaService,
)

router = APIRouter(
    prefix="/vacinas",
    tags=["Vacinas"],
)


@router.post(
    "/",
    response_model=VacinaResponse,
    status_code=HTTPStatus.CREATED,
)
def create(
    data: VacinaCreate,
    db: Session = Depends(get_db),
):
    return VacinaService.create(
        db,
        data,
    )


@router.get(
    "/",
)
def list_all(
    db: Session = Depends(get_db),
):
    return VacinaService.list_all(
        db,
    )
