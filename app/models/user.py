"""
Aqui estarão a representação das tabelas do banco.

Aqui deve ser desenvolvido :
- A criação de classes que representam tabelas (ex: Usuario, Unidade)
- A definição de colunas (id, nome, email, etc)
- A definição do relacionamentos entre tabelas

Exemplo:
class Usuario(Base):
    __tablename__ = "usuarios"
"""

from datetime import datetime
from enum import Enum

from sqlalchemy import Boolean, DateTime, String, func, text
from sqlalchemy.orm import Mapped, mapped_column, registry

from app.models.base import Base

table_registry = registry()


class StatusContaEnum(str, Enum):
    ativo = "ativo"
    inativo = "inativo"
    bloqueado = "bloqueado"


class User(Base):
    __tablename__ = "usuarios"

    id: Mapped[str] = mapped_column(
        String, primary_key=True, server_default=text("gen_random_uuid()")
    )

    nome: Mapped[str] = mapped_column(String, nullable=False)

    cpf: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    email: Mapped[str] = mapped_column(String, nullable=False)

    telefone: Mapped[str] = mapped_column(String, nullable=False)

    sexo: Mapped[str] = mapped_column(String, nullable=False)

    cartao_sus: Mapped[str | None] = mapped_column(String, nullable=True)

    senha_hash: Mapped[str] = mapped_column(String, nullable=False)

    data_nascimento: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    ativo: Mapped[bool] = mapped_column(Boolean, default=True)

    status_conta: Mapped[StatusContaEnum] = mapped_column(
        String, default=StatusContaEnum.ativo
    )

    criado_em: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now()
    )

    atualizado_em: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )
