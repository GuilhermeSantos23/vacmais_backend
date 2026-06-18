from sqlalchemy.orm import Session

from app.models.administrador_regional import (
    AdministradorRegional,
)
from app.models.user import (
    StatusContaEnum,
)
from app.schemas.administrador_regional import (
    AdministradorRegionalCreate,
)
from app.utils.security import hash_password


class AdministradorRegionalService:
    @staticmethod
    def create_admin_regional(
        db: Session,
        data: AdministradorRegionalCreate,
    ):
        admin = AdministradorRegional(
            nome=data.nome,
            cpf=data.cpf,
            email=data.email,
            telefone=data.telefone,
            registro_regional=data.registro_regional,
            regiao_id=data.regiao_id,
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
        return db.query(AdministradorRegional).all()

    @staticmethod
    def get_by_id(
        db: Session,
        admin_id: str,
    ):
        return db.get(
            AdministradorRegional,
            admin_id,
        )

    @staticmethod
    def deactivate_admin_regional(
        db: Session,
        payload: dict,
    ):
        admin = db.get(
            AdministradorRegional,
            payload["sub"],
        )

        admin.status_conta = StatusContaEnum.inativo

        db.commit()
        db.refresh(admin)

        return admin
