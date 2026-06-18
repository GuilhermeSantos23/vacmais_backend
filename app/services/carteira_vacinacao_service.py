from sqlalchemy.orm import Session

from app.models.carteira_vacinacao import (
    CarteiraVacinacao,
)
from app.schemas.carteira_vacinacao import (
    CarteiraVacinacaoCreate,
)


class CarteiraVacinacaoService:
    @staticmethod
    def create(
        db: Session,
        data: CarteiraVacinacaoCreate,
    ):
        carteira = CarteiraVacinacao(
            usuario_id=data.usuario_id,
        )

        db.add(carteira)

        db.commit()

        db.refresh(carteira)

        return carteira

    @staticmethod
    def get_by_id(
        db: Session,
        carteira_id: int,
    ):
        return db.get(
            CarteiraVacinacao,
            carteira_id,
        )

    @staticmethod
    def get_by_usuario(
        db: Session,
        usuario_id: str,
    ):
        return (
            db.query(CarteiraVacinacao)
            .filter(CarteiraVacinacao.usuario_id == usuario_id)
            .first()
        )
