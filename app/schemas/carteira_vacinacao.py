from pydantic import BaseModel


class CarteiraVacinacaoCreate(BaseModel):
    usuario_id: str


class CarteiraVacinacaoResponse(BaseModel):
    id: int
    usuario_id: str

    class Config:
        from_attributes = True
