from datetime import datetime

from sqlalchemy import (
    DateTime,
    ForeignKey,
    String,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.models.user import (
    StatusContaEnum,
    table_registry,
)


@table_registry.mapped
class AdministradorUnidade:
    __tablename__ = "administradores_unidade"

    id: Mapped[str] = mapped_column(String, primary_key=True)

    nome: Mapped[str] = mapped_column(String, nullable=False)

    cpf: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    senha_hash: Mapped[str] = mapped_column(String, nullable=False)

    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    telefone: Mapped[str] = mapped_column(String, nullable=False)

    unidade_id: Mapped[int] = mapped_column(ForeignKey("unidades.id"))

    status_conta: Mapped[StatusContaEnum] = mapped_column(
        String, default=StatusContaEnum.ativo
    )

    criado_em: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now()
    )
