from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.auth import (
    get_current_profissional,
)

from app.database.connection import get_db

from app.services.registro_vacinacao_service import (
    RegistroVacinacaoService,
)


router = APIRouter(
    prefix="/registros-vacinacao",
    tags=["Registros Vacinação"],
)


@router.post(
    "/",
    status_code=HTTPStatus.CREATED,
)
def registrar_vacina(
    data,
    db: Session = Depends(get_db),
    profissional=Depends(
        get_current_profissional
    ),
):

    return (
        RegistroVacinacaoService
        .registrar_vacina(
            db,
            data,
        )
    )