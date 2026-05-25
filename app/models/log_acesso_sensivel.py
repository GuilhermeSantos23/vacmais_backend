from datetime import datetime

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column


class LogSensivel:
    __tablename__ = "log_acesso_dados_sensiveis"

    id: Mapped[int] = mapped_column(primary_key=True)

    usuario_consultado_id: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    profissional_id: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    motivo_acesso: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    data_acesso: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
