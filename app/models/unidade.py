from datetime import datetime

from sqlalchemy import (
    DateTime,
    ForeignKey,
    Numeric,
    String,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.models.user import table_registry


@table_registry.mapped
class Unidade:
    __tablename__ = "unidades"

    id: Mapped[int] = mapped_column(primary_key=True)

    nome: Mapped[str] = mapped_column(String, nullable=False)

    tipo: Mapped[str] = mapped_column(String)

    endereco: Mapped[str] = mapped_column(String)

    cidade: Mapped[str] = mapped_column(String)

    estado: Mapped[str] = mapped_column(String)

    telefone: Mapped[str] = mapped_column(String)

    email: Mapped[str] = mapped_column(String)

    latitude: Mapped[float] = mapped_column(Numeric)

    longitude: Mapped[float] = mapped_column(Numeric)

    regiao_id: Mapped[int] = mapped_column(ForeignKey("regioes.id"))

    criado_em: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now()
    )
