from datetime import datetime

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column


class CampanhaVacinacao:
    __tablename__ = "campanhas_vacinacao"

    id: Mapped[int] = mapped_column(primary_key=True)

    titulo: Mapped[str] = mapped_column(String, nullable=False)

    descricao: Mapped[str] = mapped_column(String, nullable=False)

    data_inicio: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    data_fim: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    publico_alvo: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    vacina_id: Mapped[int] = mapped_column(nullable=False)

    regiao_id: Mapped[int] = mapped_column(nullable=False)

    criado_em: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
