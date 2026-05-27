from pydantic import BaseModel


class EstoqueCreate(BaseModel):
    lote_id: int
    unidade_id: int
    quantidade: int


class EstoqueResponse(BaseModel):
    id: int
    quantidade: int

    class Config:
        from_attributes = True
