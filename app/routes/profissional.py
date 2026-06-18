from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.auth import (
    get_current_admin_unidade,
    get_current_profissional,
)
from app.database.connection import get_db
from app.schemas.profissional import (
    ProfissionalCreate,
    ProfissionalResponse,
)
from app.services.profissional_service import (
    ProfissionalService,
)

router = APIRouter(
    prefix="/profissionais",
    tags=["Profissionais"],
)


@router.post(
    "/",
    response_model=ProfissionalResponse,
    status_code=HTTPStatus.CREATED,
)
def create_profissional(
    data: ProfissionalCreate,
    db: Session = Depends(get_db),
    admin=Depends(get_current_admin_unidade),
):
    return ProfissionalService.create(
        db,
        data,
    )


@router.get(
    "/me",
    response_model=ProfissionalResponse,
)
def get_me(
    db: Session = Depends(get_db),
    profissional=Depends(get_current_profissional),
):
    return ProfissionalService.get_by_id(
        db,
        profissional["sub"],
    )


@router.patch(
    "/deactivate",
    response_model=ProfissionalResponse,
)
def deactivate(
    db: Session = Depends(get_db),
    profissional=Depends(get_current_profissional),
):
    db_profissional = ProfissionalService.get_by_id(
        db,
        profissional["sub"],
    )

    return ProfissionalService.deactivate(
        db,
        db_profissional,
    )
