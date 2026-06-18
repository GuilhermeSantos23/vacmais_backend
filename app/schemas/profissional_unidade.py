from datetime import datetime

from pydantic import BaseModel


class ProfissionalUnidadeCreate(BaseModel):
    profissional_id: str
    unidade_id: int
    cargo: str
    data_inicio: datetime
    status_vinculo: str


class ProfissionalUnidadeResponse(BaseModel):
    id: int
    profissional_id: str
    unidade_id: int
    cargo: str
    data_inicio: datetime
    status_vinculo: str

    class Config:
        from_attributes = True
