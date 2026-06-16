from sqlalchemy.orm import Session

from app.models.estoque import Estoque


class EstoqueService:
    @staticmethod
    def atualizar_estoque(
        db: Session,
        estoque: Estoque,
        quantidade: int,
    ):
        estoque.quantidade = quantidade

        db.commit()

        db.refresh(estoque)

        return estoque
