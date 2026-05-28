from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.services.vacina_service import (
    VacinaService,
)


router = APIRouter(
    prefix="/vacinas",
    tags=["Vacinas"],
)


@router.post(
    "/",
    status_code=HTTPStatus.CREATED,
)
def create_vacina(
    data,
    db: Session = Depends(get_db),
):

    return VacinaService.create_vacina(
        db,
        data,
    )