from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.unidade import (
    UnidadeCreate,
    UnidadeResponse,
)
from app.services.unidade_service import (
    UnidadeService,
)

router = APIRouter(
    prefix="/unidades",
    tags=["Unidades"],
)


@router.post(
    "/",
    response_model=UnidadeResponse,
    status_code=HTTPStatus.CREATED,
)
def create_unidade(
    data: UnidadeCreate,
    db: Session = Depends(get_db),
):
    return UnidadeService.create(
        db,
        data,
    )


@router.get(
    "/",
    response_model=list[UnidadeResponse],
)
def list_unidades(
    db: Session = Depends(get_db),
):
    return UnidadeService.list_all(
        db,
    )


@router.get(
    "/{unidade_id}",
    response_model=UnidadeResponse,
)
def get_unidade(
    unidade_id: int,
    db: Session = Depends(get_db),
):
    return UnidadeService.get_by_id(
        db,
        unidade_id,
    )
