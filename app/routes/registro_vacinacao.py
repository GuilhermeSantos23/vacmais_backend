from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.auth import (
    get_current_profissional,
)
from app.database.connection import get_db
from app.schemas.registro_vacinacao import (
    RegistroVacinacaoCreate,
)
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
    data: RegistroVacinacaoCreate,
    db: Session = Depends(get_db),
    profissional=Depends(get_current_profissional),
):
    return RegistroVacinacaoService.registrar_vacina(
        db,
        data,
        profissional,
    )


@router.get("/usuario/{usuario_id}")
def historico_usuario(
    usuario_id: str,
    db: Session = Depends(get_db),
):
    return RegistroVacinacaoService.historico_usuario(
        db,
        usuario_id,
    )
