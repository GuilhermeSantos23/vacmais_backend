from pydantic import BaseModel


class MovimentacaoEstoqueCreate(BaseModel):
    lote_id: int
    unidade_id: int
    tipo_movimento: str
    quantidade: int


class MovimentacaoEstoqueResponse(BaseModel):
    id: int
    tipo_movimento: str
    quantidade: int

    class Config:
        from_attributes = True
