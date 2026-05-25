from datetime import datetime

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.models.user import table_registry


@table_registry.mapped
class Regiao:
    __tablename__ = "regioes"

    id: Mapped[int] = mapped_column(primary_key=True)

    nome: Mapped[str] = mapped_column(String, nullable=False)

    cidade: Mapped[str] = mapped_column(String, nullable=False)

    estado: Mapped[str] = mapped_column(String, nullable=False)

    responsavel: Mapped[str] = mapped_column(String, nullable=False)

    email: Mapped[str] = mapped_column(String, nullable=False)

    telefone: Mapped[str] = mapped_column(String, nullable=False)

    status: Mapped[str] = mapped_column(String, nullable=False)

    criado_em: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now()
    )
