from sqlalchemy.orm import Session

from app.models.registro_vacinacao import (
    RegistroVacinacao,
)


class RegistroVacinacaoService:

    @staticmethod
    def registrar_vacina(
        db: Session,
        data,
    ):

        registro = RegistroVacinacao(
            carteira_id=data.carteira_id,
            vacina_id=data.vacina_id,
            dose_numero=data.dose_numero,
            data_aplicacao=data.data_aplicacao,
            profissional_id=data.profissional_id,
            unidade_id=data.unidade_id,
            origem_registro=data.origem_registro,
            observacoes=data.observacoes,
        )

        db.add(registro)

        db.commit()

        db.refresh(registro)

        return registro