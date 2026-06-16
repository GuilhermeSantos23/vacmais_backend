from sqlalchemy.orm import Session

from app.models.regiao import Regiao
from app.schemas.regiao import (
    RegiaoCreate,
    RegiaoUpdate,
)


class RegiaoService:
    @staticmethod
    def create(
        db: Session,
        data: RegiaoCreate,
    ):
        regiao = Regiao(**data.model_dump())

        db.add(regiao)

        db.commit()

        db.refresh(regiao)

        return regiao

    @staticmethod
    def list_all(
        db: Session,
    ):
        return db.query(Regiao).all()

    @staticmethod
    def get_by_id(
        db: Session,
        regiao_id: int,
    ):
        return db.query(Regiao).filter(Regiao.id == regiao_id).first()

    @staticmethod
    def update(
        db: Session,
        regiao: Regiao,
        data: RegiaoUpdate,
    ):
        for campo, valor in data.model_dump(exclude_unset=True).items():
            setattr(
                regiao,
                campo,
                valor,
            )

        db.commit()

        db.refresh(regiao)

        return regiao
