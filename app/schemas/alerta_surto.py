from datetime import datetime

from pydantic import BaseModel


class AlertaSurtoCreate(BaseModel):
    doenca: str
    descricao: str
    nivel: str
    data_inicio: datetime
    regiao_id: int


class AlertaSurtoUpdate(BaseModel):
    descricao: str | None = None
    nivel: str | None = None


class AlertaSurtoResponse(BaseModel):
    id: int
    doenca: str
    descricao: str
    nivel: str
    data_inicio: datetime
    regiao_id: int

    class Config:
        from_attributes = True
