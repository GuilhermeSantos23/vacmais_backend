from sqlalchemy.orm import Session

from app.models.profissional import (
    Profissional,
)
from app.models.user import (
    StatusContaEnum,
)
from app.schemas.profissional import (
    ProfissionalCreate,
)
from app.utils.security import (
    hash_password,
)


class ProfissionalService:
    @staticmethod
    def create(
        db: Session,
        data: ProfissionalCreate,
    ):
        profissional = Profissional(
            nome=data.nome,
            cpf=data.cpf,
            email=data.email,
            telefone=data.telefone,
            registro_conselho=data.registro_conselho,
            conselho_profissional=data.conselho_profissional,
            senha_hash=hash_password(data.senha),
        )

        db.add(profissional)

        db.commit()

        db.refresh(profissional)

        return profissional

    @staticmethod
    def deactivate(
        db: Session,
        profissional: Profissional,
    ):
        profissional.status_conta = StatusContaEnum.inativo

        db.commit()

        db.refresh(profissional)

        return profissional

    @staticmethod
    def reactivate(
        db: Session,
        profissional: Profissional,
    ):
        profissional.status_conta = StatusContaEnum.ativo

        db.commit()

        db.refresh(profissional)

        return profissional
