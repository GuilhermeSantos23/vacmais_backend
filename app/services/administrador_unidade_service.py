from sqlalchemy.orm import Session

from app.models.administrador_unidade import (
    AdministradorUnidade,
)
from app.models.user import (
    StatusContaEnum,
)
from app.schemas.administrador_unidade import (
    AdministradorUnidadeCreate,
)
from app.utils.security import hash_password


class AdministradorUnidadeService:
    @staticmethod
    def create_admin_unidade(
        db: Session,
        data: AdministradorUnidadeCreate,
    ):
        admin = AdministradorUnidade(
            nome=data.nome,
            cpf=data.cpf,
            email=data.email,
            telefone=data.telefone,
            unidade_id=data.unidade_id,
            senha_hash=hash_password(data.senha),
        )

        db.add(admin)
        db.commit()
        db.refresh(admin)

        return admin

    @staticmethod
    def list_all(
        db: Session,
    ):
        return db.query(AdministradorUnidade).all()

    @staticmethod
    def get_by_id(
        db: Session,
        admin_id: str,
    ):
        return db.get(
            AdministradorUnidade,
            admin_id,
        )

    @staticmethod
    def deactivate_admin_unidade(
        db: Session,
        payload: dict,
    ):
        admin = db.get(
            AdministradorUnidade,
            payload["sub"],
        )

        admin.status_conta = StatusContaEnum.inativo

        db.commit()
        db.refresh(admin)

        return admin
