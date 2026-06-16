from sqlalchemy.orm import Session

from app.models.vacina import Vacina
from app.schemas.vacina import (
    VacinaCreate,
    VacinaUpdate,
)


class VacinaService:
    @staticmethod
    def create(
        db: Session,
        data: VacinaCreate,
    ):
        vacina = Vacina(**data.model_dump())

        db.add(vacina)

        db.commit()

        db.refresh(vacina)

        return vacina

    @staticmethod
    def list_all(
        db: Session,
    ):
        return db.query(Vacina).all()

    @staticmethod
    def get_by_id(
        db: Session,
        vacina_id: int,
    ):
        return db.query(Vacina).filter(Vacina.id == vacina_id).first()

    @staticmethod
    def update(
        db: Session,
        vacina: Vacina,
        data: VacinaUpdate,
    ):
        for campo, valor in data.model_dump(exclude_unset=True).items():
            setattr(
                vacina,
                campo,
                valor,
            )

        db.commit()

        db.refresh(vacina)

        return vacina
