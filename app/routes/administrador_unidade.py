from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.auth import (
    get_current_admin_regional,
    get_current_admin_unidade,
)
from app.database.connection import get_db
from app.schemas.administrador_unidade import (
    AdministradorUnidadeCreate,
    AdministradorUnidadeResponse,
)
from app.services.administrador_unidade_service import (
    AdministradorUnidadeService,
)

router = APIRouter(
    prefix="/administradores-unidade",
    tags=["Administradores Unidade"],
)


@router.post(
    "/",
    response_model=AdministradorUnidadeResponse,
    status_code=HTTPStatus.CREATED,
)
def create_admin_unidade(
    data: AdministradorUnidadeCreate,
    db: Session = Depends(get_db),
    admin=Depends(get_current_admin_regional),
):
    return AdministradorUnidadeService.create_admin_unidade(
        db,
        data,
    )


@router.get(
    "/me",
    response_model=AdministradorUnidadeResponse,
)
def get_me(
    db: Session = Depends(get_db),
    admin=Depends(get_current_admin_unidade),
):
    return AdministradorUnidadeService.get_by_id(
        db,
        admin["sub"],
    )


@router.patch(
    "/deactivate",
    response_model=AdministradorUnidadeResponse,
)
def deactivate(
    db: Session = Depends(get_db),
    admin=Depends(get_current_admin_unidade),
):
    return AdministradorUnidadeService.deactivate_admin_unidade(
        db,
        admin,
    )
