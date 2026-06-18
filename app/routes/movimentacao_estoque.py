from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.services.movimentacao_estoque_service import (
    MovimentacaoEstoqueService,
)

router = APIRouter(
    prefix="/movimentacoes-estoque",
    tags=["Movimentações Estoque"],
)


@router.get("/")
def list_all(
    db: Session = Depends(get_db),
):
    return MovimentacaoEstoqueService.list_all(db)


@router.get("/lote/{lote_id}")
def get_by_lote(
    lote_id: int,
    db: Session = Depends(get_db),
):
    return MovimentacaoEstoqueService.get_by_lote(
        db,
        lote_id,
    )
