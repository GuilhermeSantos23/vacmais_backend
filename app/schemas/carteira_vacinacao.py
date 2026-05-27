from pydantic import BaseModel


class CarteiraVacinacaoCreate(BaseModel):
    cidadao_id: str


class CarteiraVacinacaoResponse(BaseModel):
    id: int
    cidadao_id: str

    class Config:
        from_attributes = True
