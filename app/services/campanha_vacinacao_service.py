from sqlalchemy.orm import Session

from app.models.campanha_vacinacao import (
    CampanhaVacinacao,
)
from app.schemas.campanha_vacinacao import (
    CampanhaVacinacaoCreate,
)


class CampanhaVacinacaoService:
    @staticmethod
    def create(
        db: Session,
        data: CampanhaVacinacaoCreate,
    ):
        campanha = CampanhaVacinacao(
            titulo=data.titulo,
            descricao=data.descricao,
            data_inicio=data.data_inicio,
            data_fim=data.data_fim,
            publico_alvo=data.publico_alvo,
            vacina_id=data.vacina_id,
            regiao_id=data.regiao_id,
        )

        db.add(campanha)
        db.commit()
        db.refresh(campanha)

        return campanha

    @staticmethod
    def get_all(db: Session):
        return db.query(CampanhaVacinacao).all()
