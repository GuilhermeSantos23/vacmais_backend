"""
Aqui é onde entra a regra de negócio da aplicação.

Aqui deve ser desenvolvido:
- O processamento de dados antes de salvar
- A aplicação das regras (ex: validações complexas)
- E a separação lógica do endpoint

IMPORTANTE:
Routes NÃO devem ter lógica, apenas chamar services.
"""

from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.security import hash_password


class UserService:
    @staticmethod
    def create_user(
        db: Session,
        data: UserCreate,
    ):
        user = User(
            nome=data.nome,
            cpf=data.cpf,
            email=data.email,
            telefone=data.telefone,
            sexo=data.sexo,
            cartao_sus=data.cartao_sus,
            senha_hash=hash_password(data.senha),
            data_nascimento=data.data_nascimento,
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    @staticmethod
    def get_by_id(
        db: Session,
        user_id: str,
    ):
        return db.get(User, user_id)

    @staticmethod
    def deactivate_user(
        db: Session,
        payload: dict,
    ):
        user = db.get(
            User,
            payload["sub"],
        )

        user.ativo = False

        db.commit()
        db.refresh(user)

        return user
