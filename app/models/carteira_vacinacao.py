from datetime import datetime

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column


class CarteiraVacinacao:
    __tablename__ = "carteiras_vacinacao"

    id: Mapped[int] = mapped_column(primary_key=True)

    usuario_id: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    criado_em: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
