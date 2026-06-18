from datetime import datetime

from sqlalchemy import (
    DateTime,
    ForeignKey,
    String,
    Text,
    func,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from app.models.user import table_registry


@table_registry.mapped
class CondicaoVacinaRestrita:
    __tablename__ = "condicoes_vacinas_restritas"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    tipo_condicao: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    vacina_id: Mapped[int] = mapped_column(
        ForeignKey("vacinas.id"),
        nullable=False,
    )

    motivo: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    criado_em: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
