from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.auth import (
    get_current_admin_regional,
)
from app.database.connection import get_db
from app.schemas.administrador_regional import (
    AdministradorRegionalCreate,
    AdministradorRegionalResponse,
)
from app.services.administrador_regional_service import (
    AdministradorRegionalService,
)

router = APIRouter(
    prefix="/administradores-regionais",
    tags=["Administradores Regionais"],
)


@router.post(
    "/",
    response_model=AdministradorRegionalResponse,
    status_code=HTTPStatus.CREATED,
)
def create_admin(
    data: AdministradorRegionalCreate,
    db: Session = Depends(get_db),
):
    return AdministradorRegionalService.create(
        db,
        data,
    )


@router.get(
    "/me",
    response_model=AdministradorRegionalResponse,
)
def get_me(
    db: Session = Depends(get_db),
    admin=Depends(get_current_admin_regional),
):
    return AdministradorRegionalService.get_by_id(
        db,
        admin["sub"],
    )


@router.patch(
    "/deactivate",
    response_model=AdministradorRegionalResponse,
)
def deactivate(
    db: Session = Depends(get_db),
    admin=Depends(get_current_admin_regional),
):
    db_admin = AdministradorRegionalService.get_by_id(
        db,
        admin["sub"],
    )

    return AdministradorRegionalService.deactivate(
        db,
        db_admin,
    )
