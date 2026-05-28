from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.auth import (
    get_current_admin_regional,
)

from app.database.connection import get_db

from app.services.administrador_regional_service import (
    AdministradorRegionalService,
)


router = APIRouter(
    prefix="/administradores-regionais",
    tags=["Administradores Regionais"],
)


@router.get("/me")
def get_me(
    admin=Depends(
        get_current_admin_regional
    )
):

    return admin


@router.patch("/deactivate")
def deactivate(
    db: Session = Depends(get_db),
    admin=Depends(
        get_current_admin_regional
    )
):

    return (
        AdministradorRegionalService
        .deactivate_admin_regional(
            db,
            admin,
        )
    )