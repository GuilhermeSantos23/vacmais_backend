from datetime import datetime

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column


class InformativoSaude:
    __tablename__ = "informativos_saude"

    id: Mapped[int] = mapped_column(primary_key=True)

    titulo: Mapped[str] = mapped_column(String, nullable=False)

    conteudo: Mapped[str] = mapped_column(String, nullable=False)

    tipo: Mapped[str] = mapped_column(String, nullable=False)

    autor_id: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    publicado_em: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
