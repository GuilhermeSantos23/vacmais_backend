from sqlalchemy.orm import Session

from app.models.movimentacao_estoque import (
    MovimentacaoEstoque,
)
from app.schemas.movimentacao_estoque import (
    MovimentacaoEstoqueCreate,
)


class MovimentacaoEstoqueService:
    @staticmethod
    def criar_movimentacao(
        db: Session,
        data: MovimentacaoEstoqueCreate,
    ):
        movimentacao = MovimentacaoEstoque(
            lote_id=data.lote_id,
            unidade_id=data.unidade_id,
            responsavel_id=data.responsavel_id,
            tipo_movimento=data.tipo_movimento,
            quantidade=data.quantidade,
            nota_fiscal_url=data.nota_fiscal_url,
        )

        db.add(movimentacao)

        db.commit()

        db.refresh(movimentacao)

        return movimentacao

    @staticmethod
    def listar(
        db: Session,
    ):
        return db.query(MovimentacaoEstoque).all()

    @staticmethod
    def get_by_id(
        db: Session,
        movimentacao_id: int,
    ):
        return db.get(
            MovimentacaoEstoque,
            movimentacao_id,
        )
