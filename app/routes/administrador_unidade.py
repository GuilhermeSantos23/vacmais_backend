from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.auth import (
    get_current_admin_unidade,
)

from app.database.connection import get_db

from app.services.administrador_unidade_service import (
    AdministradorUnidadeService,
)


router = APIRouter(
    prefix="/administradores-unidade",
    tags=["Administradores Unidade"],
)


@router.get("/me")
def get_me(
    admin=Depends(
        get_current_admin_unidade
    )
):

    return admin


@router.patch("/deactivate")
def deactivate(
    db: Session = Depends(get_db),
    admin=Depends(
        get_current_admin_unidade
    )
):

    return (
        AdministradorUnidadeService
        .deactivate_admin_unidade(
            db,
            admin,
        )
    )