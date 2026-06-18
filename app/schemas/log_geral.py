from datetime import datetime

from pydantic import BaseModel


class LogGeralResponse(BaseModel):
    id: int
    usuario_tipo: str
    usuario_id: str
    acao: str
    entidade_afetada: str
    data_acao: datetime

    class Config:
        from_attributes = True
