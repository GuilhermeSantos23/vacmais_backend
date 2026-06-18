from sqlalchemy.orm import Session

from app.models.condicao_sensivel import CondicaoSensivel
from app.schemas.condicao_sensivel import (
    CondicaoSensivelCreate,
)


class CondicaoSensivelService:
    @staticmethod
    def create(
        db: Session,
        data: CondicaoSensivelCreate,
    ):
        condicao = CondicaoSensivel(
            usuario_id=data.usuario_id,
            profissional_registro_id=data.profissional_registro_id,
            tipo_condicao=data.tipo_condicao,
            descricao=data.descricao,
        )

        db.add(condicao)

        db.commit()

        db.refresh(condicao)

        return condicao

    @staticmethod
    def listar_por_usuario(
        db: Session,
        usuario_id: str,
    ):
        return (
            db.query(CondicaoSensivel)
            .filter(CondicaoSensivel.usuario_id == usuario_id)
            .all()
        )
