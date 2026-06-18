from sqlalchemy.orm import Session

from app.models.profissional_obrigatoriedade_vacinal import (
    ProfissionalObrigatoriedadeVacinal,
)
from app.schemas.profissional_obrigatoriedade_vacinal import (
    ProfissionalObrigatoriedadeVacinalCreate,
)


class ProfissionalObrigatoriedadeVacinalService:
    @staticmethod
    def create(
        db: Session,
        data: ProfissionalObrigatoriedadeVacinalCreate,
    ):
        registro = ProfissionalObrigatoriedadeVacinal(
            profissional_id=data.profissional_id,
            vacina_id=data.vacina_id,
            obrigatoria=True,
        )

        db.add(registro)

        db.commit()

        db.refresh(registro)

        return registro

    @staticmethod
    def listar_por_profissional(
        db: Session,
        profissional_id: str,
    ):
        return (
            db.query(ProfissionalObrigatoriedadeVacinal)
            .filter(
                ProfissionalObrigatoriedadeVacinal.profissional_id
                == profissional_id
            )
            .all()
        )
