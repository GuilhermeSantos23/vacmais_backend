from datetime import datetime
from enum import Enum

from sqlalchemy import DateTime, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column


class TipoMovimentoEnum(str, Enum):
    entrada = "entrada"
    saida = "saida"
    perda = "perda"


class MovimentacaoEstoque:
    __tablename__ = "movimentacao_estoque"

    id: Mapped[int] = mapped_column(primary_key=True)

    lote_id: Mapped[int] = mapped_column(nullable=False)

    unidade_id: Mapped[int] = mapped_column(nullable=False)

    responsavel_id: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    tipo_movimento: Mapped[TipoMovimentoEnum] = mapped_column(
        String,
        nullable=False,
    )

    quantidade: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    nota_fiscal_url: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    data_movimento: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
