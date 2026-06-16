from sqlalchemy.orm import Session

from app.models.informativo_saude import (
    InformativoSaude,
)
from app.schemas.informativo_saude import (
    InformativoSaudeCreate,
)


class InformativoSaudeService:
    @staticmethod
    def create(
        db: Session,
        data: InformativoSaudeCreate,
    ):
        informativo = InformativoSaude(
            titulo=data.titulo,
            conteudo=data.conteudo,
            tipo=data.tipo,
            autor_id=data.autor_id,
        )

        db.add(informativo)
        db.commit()
        db.refresh(informativo)

        return informativo

    @staticmethod
    def get_all(
        db: Session,
    ):
        return db.query(InformativoSaude).all()
