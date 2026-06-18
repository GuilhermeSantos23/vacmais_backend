from datetime import datetime

from pydantic import BaseModel

# class CampanhaVacinacaoCreate(BaseModel):
#    titulo: str
#    descricao: str
#    publico_alvo: str


class CampanhaVacinacaoCreate(BaseModel):
    titulo: str
    descricao: str
    data_inicio: datetime
    data_fim: datetime
    publico_alvo: str
    vacina_id: int
    regiao_id: int


class CampanhaVacinacaoUpdate(BaseModel):
    titulo: str | None = None
    descricao: str | None = None
    publico_alvo: str | None = None


class CampanhaVacinacaoResponse(BaseModel):
    id: int
    titulo: str
    descricao: str
    data_inicio: datetime
    data_fim: datetime
    publico_alvo: str
    vacina_id: int
    regiao_id: int

    class Config:
        from_attributes = True
