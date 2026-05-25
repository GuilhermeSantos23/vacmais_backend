from datetime import datetime

from sqlalchemy import DateTime, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column


class RegistroVacinacao:
    __tablename__ = "registros_vacinacao"

    id: Mapped[int] = mapped_column(primary_key=True)

    carteira_id: Mapped[int] = mapped_column(nullable=False)

    vacina_id: Mapped[int] = mapped_column(nullable=False)

    dose_numero: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    data_aplicacao: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    profissional_id: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    unidade_id: Mapped[int] = mapped_column(nullable=False)

    origem_registro: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    observacoes: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    criado_em: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
