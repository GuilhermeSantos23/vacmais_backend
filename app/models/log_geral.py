from datetime import datetime

from sqlalchemy import JSON, DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column


class LogGeral:
    __tablename__ = "log_geral"

    id: Mapped[int] = mapped_column(primary_key=True)

    usuario_tipo: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    usuario_id: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    acao: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    entidade_afetada: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    registro_afetado_id: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    dados_anteriores: Mapped[dict] = mapped_column(
        JSON,
        nullable=True,
    )

    dados_novos: Mapped[dict] = mapped_column(
        JSON,
        nullable=True,
    )

    ip: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    user_agent: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    data_acao: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
