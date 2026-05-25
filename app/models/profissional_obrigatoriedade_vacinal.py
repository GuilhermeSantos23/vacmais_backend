from datetime import datetime

from sqlalchemy import Boolean, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column


class ProfissionalObrigatoriedadeVacinal:
    __tablename__ = "profissionais_obrigatoriedade_vacinal"

    id: Mapped[int] = mapped_column(primary_key=True)

    profissional_id: Mapped[str] = mapped_column(
        nullable=False,
    )

    vacina_id: Mapped[int] = mapped_column(nullable=False)

    obrigatoria: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    atualizado_em: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
