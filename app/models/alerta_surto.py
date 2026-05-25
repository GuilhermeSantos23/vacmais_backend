from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column


class AlertaSurto:
    __tablename__ = "alertas_surtos"

    id: Mapped[int] = mapped_column(primary_key=True)

    doenca: Mapped[str] = mapped_column(String, nullable=False)

    descricao: Mapped[str] = mapped_column(String, nullable=False)

    nivel: Mapped[str] = mapped_column(String, nullable=False)

    data_inicio: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    regiao_id: Mapped[int] = mapped_column(nullable=False)
