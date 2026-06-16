from datetime import datetime

from pydantic import BaseModel


class AlertaSurtoCreate(BaseModel):
    doenca: str
    descricao: str
    nivel: str
    data_inicio: datetime
    regiao_id: int


class AlertaSurtoResponse(BaseModel):
    id: int
    doenca: str
    nivel: str

    class Config:
        from_attributes = True
