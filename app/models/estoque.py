from datetime import datetime

from sqlalchemy import DateTime, Integer, func
from sqlalchemy.orm import Mapped, mapped_column


class Estoque:
    __tablename__ = "estoque"

    id: Mapped[int] = mapped_column(primary_key=True)

    lote_id: Mapped[int] = mapped_column(nullable=False)

    unidade_id: Mapped[int] = mapped_column(nullable=False)

    quantidade: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    atualizado_em: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
