from pydantic import BaseModel


class MovimentacaoEstoqueCreate(BaseModel):
    lote_id: int
    unidade_id: int
    responsavel_id: str
    tipo_movimento: str
    quantidade: int
    nota_fiscal_url: str


class MovimentacaoEstoqueResponse(BaseModel):
    id: int
    tipo_movimento: str
    quantidade: int

    class Config:
        from_attributes = True
