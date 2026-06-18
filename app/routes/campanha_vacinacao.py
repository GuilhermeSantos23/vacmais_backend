from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.campanha_vacinacao import (
    CampanhaVacinacaoCreate,
)
from app.services.campanha_vacinacao_service import (
    CampanhaVacinacaoService,
)

router = APIRouter(
    prefix="/campanhas",
    tags=["Campanhas"],
)


@router.post(
    "/",
    status_code=HTTPStatus.CREATED,
)
def create(
    data: CampanhaVacinacaoCreate,
    db: Session = Depends(get_db),
):
    return CampanhaVacinacaoService.create(
        db,
        data,
    )


@router.get("/")
def list_all(
    db: Session = Depends(get_db),
):
    return CampanhaVacinacaoService.get_all(
        db,
    )


@router.delete("/{campanha_id}")
def delete(
    campanha_id: int,
    db: Session = Depends(get_db),
):
    return CampanhaVacinacaoService.delete(
        db,
        campanha_id,
    )
