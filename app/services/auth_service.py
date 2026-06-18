from sqlalchemy.orm import Session

from app.models.administrador_regional import (
    AdministradorRegional,
)
from app.models.administrador_unidade import (
    AdministradorUnidade,
)
from app.models.profissional import (
    Profissional,
)
from app.models.user import (
    StatusContaEnum,
    User,
)
from app.utils.security import (
    create_access_token,
    verify_password,
)


class AuthService:
    @staticmethod
    def authenticate(
        db: Session,
        email: str,
        senha: str,
    ):
        usuario = db.query(User).filter(User.email == email).first()

        tipo = "user"

        if not usuario:
            usuario = (
                db.query(Profissional)
                .filter(Profissional.email == email)
                .first()
            )

            tipo = "profissional"

        if not usuario:
            usuario = (
                db.query(AdministradorUnidade)
                .filter(AdministradorUnidade.email == email)
                .first()
            )

            tipo = "admin_unidade"

        if not usuario:
            usuario = (
                db.query(AdministradorRegional)
                .filter(AdministradorRegional.email == email)
                .first()
            )

            tipo = "admin_regional"

        if not usuario:
            return None

        if tipo == "user":
            if not usuario.ativo:
                return None
        elif usuario.status_conta != StatusContaEnum.ativo:
            return None

        senha_valida = verify_password(
            senha,
            usuario.senha_hash,
        )

        if not senha_valida:
            return None

        token = create_access_token(
            {
                "sub": str(usuario.id),
                "tipo": tipo,
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer",
        }
