from pydantic import BaseModel


class CampanhaVacinacaoCreate(BaseModel):
    titulo: str
    descricao: str
    publico_alvo: str


class CampanhaVacinacaoResponse(BaseModel):
    id: int
    titulo: str
    publico_alvo: str

    class Config:
        from_attributes = True
