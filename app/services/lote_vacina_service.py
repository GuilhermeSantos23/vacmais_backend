from sqlalchemy.orm import Session

from app.models.lote_vacina import LoteVacina
from app.schemas.lote_vacina import (
    LoteVacinaCreate,
)


class LoteVacinaService:
    @staticmethod
    def create_lote(
        db: Session,
        data: LoteVacinaCreate,
    ):
        lote = LoteVacina(
            vacina_id=data.vacina_id,
            lote=data.lote,
            fabricante=data.fabricante,
            data_validade=data.data_validade,
        )

        db.add(lote)
        db.commit()
        db.refresh(lote)

        return lote

    @staticmethod
    def get_by_id(
        db: Session,
        lote_id: int,
    ):
        return db.get(
            LoteVacina,
            lote_id,
        )
