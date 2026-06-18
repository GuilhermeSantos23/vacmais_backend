from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.informativo_saude import (
    InformativoSaudeCreate,
)
from app.services.informativo_saude_service import (
    InformativoSaudeService,
)

router = APIRouter(
    prefix="/informativos",
    tags=["Informativos"],
)


@router.post(
    "/",
    status_code=HTTPStatus.CREATED,
)
def create(
    data: InformativoSaudeCreate,
    db: Session = Depends(get_db),
):
    return InformativoSaudeService.create(
        db,
        data,
    )


@router.get("/")
def list_all(
    db: Session = Depends(get_db),
):
    return InformativoSaudeService.get_all(
        db,
    )


@router.delete("/{informativo_id}")
def delete(
    informativo_id: int,
    db: Session = Depends(get_db),
):
    return InformativoSaudeService.delete(
        db,
        informativo_id,
    )
