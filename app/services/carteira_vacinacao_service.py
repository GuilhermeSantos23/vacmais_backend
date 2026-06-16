from sqlalchemy.orm import Session

from app.models.carteira_vacinacao import (
    CarteiraVacinacao,
)


class CarteiraVacinacaoService:
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
