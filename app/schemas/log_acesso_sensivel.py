from datetime import datetime

from pydantic import BaseModel


class LogSensivelResponse(BaseModel):
    id: int
    usuario_consultado_id: str
    profissional_id: str
    motivo_acesso: str
    data_acesso: datetime

    class Config:
        from_attributes = True
