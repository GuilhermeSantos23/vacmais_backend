from datetime import datetime

from pydantic import BaseModel


class RegistroVacinacaoCreate(BaseModel):
    carteira_id: int
    vacina_id: int
    dose_numero: int
    data_aplicacao: datetime
    profissional_id: str
    unidade_id: int
    origem_registro: str
    observacoes: str


class RegistroVacinacaoResponse(BaseModel):
    id: int
    carteira_id: int
    vacina_id: int
    dose_numero: int
    data_aplicacao: datetime
    profissional_id: str
    unidade_id: int
    origem_registro: str
    observacoes: str

    class Config:
        from_attributes = True
