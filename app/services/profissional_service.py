from sqlalchemy.orm import Session

from app.models.profissional import (
    Profissional,
)

from app.utils.security import (
    hash_password,
)


class ProfissionalService:

    @staticmethod
    def create_profissional(
        db: Session,
        data,
    ):

        profissional = Profissional(
            nome=data.nome,
            cpf=data.cpf,
            email=data.email,
            telefone=data.telefone,
            registro_conselho=data.registro_conselho,
            conselho_profissional=data.conselho_profissional,
            senha_hash=hash_password(
                data.senha
            ),
        )

        db.add(profissional)

        db.commit()

        db.refresh(profissional)

        return profissional

    @staticmethod
    def deactivate_profissional(
        db: Session,
        profissional,
    ):

        profissional.ativo = False

        db.commit()

        db.refresh(profissional)

        return profissional