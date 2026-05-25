from datetime import datetime

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column


class CondicaoSensivel:
    __tablename__ = "condicoes_sensiveis"

    id: Mapped[int] = mapped_column(primary_key=True)

    usuario_id: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    profissional_registro_id: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    tipo_condicao: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    descricao: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    data_registro: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
