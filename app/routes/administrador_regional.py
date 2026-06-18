from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.auth import (
    get_current_admin_regional,
)
from app.database.connection import get_db
from app.schemas.administrador_regional import (
    AdministradorRegionalResponse,
)
from app.services.administrador_regional_service import (
    AdministradorRegionalService,
)

router = APIRouter(
    prefix="/administradores-regionais",
    tags=["Administradores Regionais"],
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
    return AdministradorRegionalService.deactivate_admin_regional(
        db,
        admin,
    )
