from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.regiao import (
    RegiaoCreate,
    RegiaoResponse,
)
from app.services.regiao_service import (
    RegiaoService,
)

router = APIRouter(
    prefix="/regioes",
    tags=["Regiões"],
)


@router.post(
    "/",
    response_model=RegiaoResponse,
    status_code=HTTPStatus.CREATED,
)
def create_regiao(
    data: RegiaoCreate,
    db: Session = Depends(get_db),
):
    return RegiaoService.create(
        db,
        data,
    )


@router.get(
    "/",
    response_model=list[RegiaoResponse],
)
def list_regioes(
    db: Session = Depends(get_db),
):
    return RegiaoService.list_all(
        db,
    )


@router.get(
    "/{regiao_id}",
    response_model=RegiaoResponse,
)
def get_regiao(
    regiao_id: int,
    db: Session = Depends(get_db),
):
    return RegiaoService.get_by_id(
        db,
        regiao_id,
    )
