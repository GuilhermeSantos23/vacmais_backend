from datetime import datetime

from sqlalchemy import (
    Boolean,
    DateTime,
    String,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.models.user import (
    StatusContaEnum,
    table_registry,
)


@table_registry.mapped
class Profissional:
    __tablename__ = "profissionais"

    id: Mapped[str] = mapped_column(String, primary_key=True)

    nome: Mapped[str] = mapped_column(String, nullable=False)

    cpf: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    senha_hash: Mapped[str] = mapped_column(String, nullable=False)

    telefone: Mapped[str] = mapped_column(String, nullable=False)

    registro_conselho: Mapped[str] = mapped_column(String, nullable=False)

    conselho_profissional: Mapped[str] = mapped_column(String, nullable=False)

    validado_profissional: Mapped[bool] = mapped_column(Boolean, default=False)

    status_conta: Mapped[StatusContaEnum] = mapped_column(
        String, default=StatusContaEnum.ativo
    )

    criado_em: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now()
    )
