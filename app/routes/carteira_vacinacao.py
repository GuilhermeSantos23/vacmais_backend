from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.services.carteira_vacinacao_service import (
    CarteiraVacinacaoService,
)

router = APIRouter(
    prefix="/carteiras",
    tags=["Carteiras Vacinação"],
)


@router.get("/usuario/{usuario_id}")
def buscar_carteira(
    usuario_id: str,
    db: Session = Depends(get_db),
):
    return CarteiraVacinacaoService.buscar_por_usuario(
        db,
        usuario_id,
    )
