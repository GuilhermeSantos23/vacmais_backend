from sqlalchemy.orm import Session

from app.models.unidade import Unidade
from app.schemas.unidade import (
    UnidadeCreate,
)


class UnidadeService:
    @staticmethod
    def create(
        db: Session,
        data: UnidadeCreate,
    ):
        unidade = Unidade(**data.model_dump())

        db.add(unidade)
        db.commit()
        db.refresh(unidade)

        return unidade

    @staticmethod
    def list_all(
        db: Session,
    ):
        return db.query(Unidade).all()

    @staticmethod
    def get_by_id(
        db: Session,
        unidade_id: int,
    ):
        return db.get(
            Unidade,
            unidade_id,
        )

    @staticmethod
    def update(
        db: Session,
        unidade: Unidade,
        data,
    ):
        for campo, valor in data.model_dump(
            exclude_unset=True,
        ).items():
            setattr(
                unidade,
                campo,
                valor,
            )

        db.commit()
        db.refresh(unidade)

        return unidade
