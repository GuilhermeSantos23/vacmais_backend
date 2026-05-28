from sqlalchemy.orm import Session

from app.models.administrador_unidade import (
    AdministradorUnidade,
)

from app.utils.security import (
    hash_password,
)


class AdministradorUnidadeService:

    @staticmethod
    def create_admin_unidade(
        db: Session,
        data,
    ):

        admin = AdministradorUnidade(
            nome=data.nome,
            cpf=data.cpf,
            email=data.email,
            telefone=data.telefone,
            unidade_id=data.unidade_id,
            senha_hash=hash_password(
                data.senha
            ),
        )

        db.add(admin)

        db.commit()

        db.refresh(admin)

        return admin

    @staticmethod
    def deactivate_admin_unidade(
        db: Session,
        admin,
    ):

        admin.ativo = False

        db.commit()

        db.refresh(admin)

        return admin