from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.auth import (
    get_current_profissional,
)

from app.database.connection import get_db

from app.services.profissional_service import (
    ProfissionalService,
)


router = APIRouter(
    prefix="/profissionais",
    tags=["Profissionais"],
)


# =========================
# GET ME
# =========================

@router.get("/me")
def get_me(
    profissional=Depends(
        get_current_profissional
    )
):

    return profissional


# =========================
# DEACTIVATE
# =========================

@router.patch("/deactivate")
def deactivate(
    db: Session = Depends(get_db),
    profissional=Depends(
        get_current_profissional
    )
):

    return ProfissionalService.deactivate_profissional(
        db,
        profissional,
    )