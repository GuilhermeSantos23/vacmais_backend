from sqlalchemy.orm import Session

from app.models.administrador_regional import (
    AdministradorRegional,
)

from app.utils.security import (
    hash_password,
)


class AdministradorRegionalService:

    @staticmethod
    def create_admin_regional(
        db: Session,
        data,
    ):

        admin = AdministradorRegional(
            nome=data.nome,
            cpf=data.cpf,
            email=data.email,
            telefone=data.telefone,
            registro_regional=data.registro_regional,
            regiao_id=data.regiao_id,
            senha_hash=hash_password(
                data.senha
            ),
        )

        db.add(admin)

        db.commit()

        db.refresh(admin)

        return admin

    @staticmethod
    def deactivate_admin_regional(
        db: Session,
        admin,
    ):

        admin.ativo = False

        db.commit()

        db.refresh(admin)

        return admin