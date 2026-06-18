from sqlalchemy.orm import Session

from app.models.estoque import Estoque
from app.schemas.estoque import EstoqueCreate


class EstoqueService:
    @staticmethod
    def create(
        db: Session,
        data: EstoqueCreate,
    ):
        estoque = Estoque(
            lote_id=data.lote_id,
            unidade_id=data.unidade_id,
            quantidade=data.quantidade,
        )

        db.add(estoque)

        db.commit()

        db.refresh(estoque)

        return estoque

    @staticmethod
    def list_all(
        db: Session,
    ):
        return db.query(Estoque).all()

    @staticmethod
    def get_by_id(
        db: Session,
        estoque_id: int,
    ):
        return db.get(
            Estoque,
            estoque_id,
        )

    @staticmethod
    def get_by_lote(
        db: Session,
        lote_id: int,
    ):
        return db.query(Estoque).filter(Estoque.lote_id == lote_id).first()

    @staticmethod
    def update(
        db: Session,
        estoque: Estoque,
        quantidade: int,
    ):
        estoque.quantidade = quantidade

        db.commit()

        db.refresh(estoque)

        return estoque

    @staticmethod
    def baixar_estoque(
        db: Session,
        estoque: Estoque,
        quantidade: int,
    ):
        if estoque.quantidade < quantidade:
            raise ValueError("Estoque insuficiente")

        estoque.quantidade -= quantidade

        db.commit()

        db.refresh(estoque)

        return estoque
