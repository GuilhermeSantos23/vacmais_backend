from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.vacina import (
    VacinaCreate,
    VacinaResponse,
    VacinaUpdate,
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
def create_vacina(
    data: VacinaCreate,
    db: Session = Depends(get_db),
):
    return VacinaService.create(
        db,
        data,
    )


@router.get(
    "/",
    response_model=list[VacinaResponse],
)
def list_vacinas(
    db: Session = Depends(get_db),
):
    return VacinaService.list_all(
        db,
    )


@router.get(
    "/{vacina_id}",
    response_model=VacinaResponse,
)
def get_vacina(
    vacina_id: int,
    db: Session = Depends(get_db),
):
    return VacinaService.get_by_id(
        db,
        vacina_id,
    )


@router.put(
    "/{vacina_id}",
    response_model=VacinaResponse,
)
def update_vacina(
    vacina_id: int,
    data: VacinaUpdate,
    db: Session = Depends(get_db),
):
    vacina = VacinaService.get_by_id(
        db,
        vacina_id,
    )

    return VacinaService.update(
        db,
        vacina,
        data,
    )
