from datetime import datetime

from sqlalchemy import (
    Boolean,
    DateTime,
    Integer,
    String,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.models.user import table_registry


@table_registry.mapped
class Vacina:
    __tablename__ = "vacinas"

    id: Mapped[int] = mapped_column(primary_key=True)

    nome: Mapped[str] = mapped_column(String, nullable=False)

    descricao: Mapped[str] = mapped_column(String)

    doses_necessarias: Mapped[int] = mapped_column(Integer)

    intervalo_dias: Mapped[int] = mapped_column(Integer)

    faixa_etaria_min: Mapped[int] = mapped_column(Integer)

    faixa_etaria_max: Mapped[int] = mapped_column(Integer)

    obrigatoria: Mapped[bool] = mapped_column(Boolean, default=False)

    criado_em: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now()
    )
