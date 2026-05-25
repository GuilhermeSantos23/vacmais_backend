from datetime import datetime

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column


class LoteVacina:
    __tablename__ = "lotes_vacina"

    id: Mapped[int] = mapped_column(primary_key=True)

    vacina_id: Mapped[int] = mapped_column(nullable=False)

    lote: Mapped[str] = mapped_column(String, nullable=False)

    fabricante: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    data_validade: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    criado_em: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
