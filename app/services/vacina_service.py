from sqlalchemy.orm import Session

from app.models.vacina import Vacina


class VacinaService:

    @staticmethod
    def create_vacina(
        db: Session,
        data,
    ):

        vacina = Vacina(
            nome=data.nome,
            descricao=data.descricao,
            doses_necessarias=data.doses_necessarias,
            intervalo_dias=data.intervalo_dias,
            faixa_etaria_min=data.faixa_etaria_min,
            faixa_etaria_max=data.faixa_etaria_max,
            obrigatoria=data.obrigatoria,
        )

        db.add(vacina)

        db.commit()

        db.refresh(vacina)

        return vacina