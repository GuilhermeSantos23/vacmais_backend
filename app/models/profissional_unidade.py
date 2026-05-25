from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column


class ProfissionalUnidade:
    __tablename__ = "profissionais_unidades"

    id: Mapped[int] = mapped_column(primary_key=True)

    profissional_id: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    unidade_id: Mapped[int] = mapped_column(nullable=False)

    cargo: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    data_inicio: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    status_vinculo: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
