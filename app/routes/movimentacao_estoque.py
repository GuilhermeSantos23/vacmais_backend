from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.movimentacao_estoque import (
    MovimentacaoEstoqueCreate,
    MovimentacaoEstoqueResponse,
)
from app.services.movimentacao_estoque_service import (
    MovimentacaoEstoqueService,
)

router = APIRouter(
    prefix="/movimentacoes-estoque",
    tags=["Movimentações de Estoque"],
)


@router.post(
    "/",
    response_model=MovimentacaoEstoqueResponse,
    status_code=HTTPStatus.CREATED,
)
def create(
    data: MovimentacaoEstoqueCreate,
    db: Session = Depends(get_db),
):
    return MovimentacaoEstoqueService.create(
        db,
        data,
    )


@router.get("/")
def list_all(
    db: Session = Depends(get_db),
):
    return MovimentacaoEstoqueService.list_all(
        db,
    )
