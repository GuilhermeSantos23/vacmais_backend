from sqlalchemy.orm import Session

from app.models.condicao_vacina_restrita import (
    CondicaoVacinaRestrita,
)
from app.schemas.condicao_vacina_restrita import (
    CondicaoVacinaRestritaCreate,
)


class CondicaoVacinaRestritaService:
    @staticmethod
    def create(
        db: Session,
        data: CondicaoVacinaRestritaCreate,
    ):
        registro = CondicaoVacinaRestrita(
            tipo_condicao=data.tipo_condicao,
            vacina_id=data.vacina_id,
            motivo=data.motivo,
        )

        db.add(registro)

        db.commit()

        db.refresh(registro)

        return registro

    @staticmethod
    def list_all(
        db: Session,
    ):
        return db.query(CondicaoVacinaRestrita).all()

    @staticmethod
    def get_by_condicao(
        db: Session,
        tipo_condicao: str,
    ):
        return (
            db.query(CondicaoVacinaRestrita)
            .filter(CondicaoVacinaRestrita.tipo_condicao == tipo_condicao)
            .all()
        )

    @staticmethod
    def delete(
        db: Session,
        registro: CondicaoVacinaRestrita,
    ):
        db.delete(registro)

        db.commit()
