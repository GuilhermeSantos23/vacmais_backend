from sqlalchemy.orm import Session

from app.models.alerta_surto import (
    AlertaSurto,
)
from app.schemas.alerta_surto import (
    AlertaSurtoCreate,
)


class AlertaSurtoService:
    @staticmethod
    def create(
        db: Session,
        data: AlertaSurtoCreate,
    ):
        alerta = AlertaSurto(
            doenca=data.doenca,
            descricao=data.descricao,
            nivel=data.nivel,
            data_inicio=data.data_inicio,
            regiao_id=data.regiao_id,
        )

        db.add(alerta)
        db.commit()
        db.refresh(alerta)

        return alerta

    @staticmethod
    def get_all(db: Session):
        return db.query(AlertaSurto).all()
