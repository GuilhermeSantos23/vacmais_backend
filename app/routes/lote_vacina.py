from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.lote_vacina import (
    LoteVacinaCreate,
    LoteVacinaResponse,
)
from app.services.lote_vacina_service import (
    LoteVacinaService,
)

router = APIRouter(
    prefix="/lotes-vacina",
    tags=["Lotes Vacina"],
)


@router.post(
    "/",
    response_model=LoteVacinaResponse,
    status_code=HTTPStatus.CREATED,
)
def create(
    data: LoteVacinaCreate,
    db: Session = Depends(get_db),
):
    return LoteVacinaService.create_lote(
        db,
        data,
    )


@router.get("/")
def list_all(
    db: Session = Depends(get_db),
):
    return LoteVacinaService.list_all(db)


@router.get("/{lote_id}")
def get_by_id(
    lote_id: int,
    db: Session = Depends(get_db),
):
    return LoteVacinaService.get_by_id(
        db,
        lote_id,
    )
