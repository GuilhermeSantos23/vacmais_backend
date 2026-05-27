from pydantic import BaseModel


class RegistroVacinacaoCreate(BaseModel):
    carteira_id: int
    vacina_id: int
    dose_numero: int


class RegistroVacinacaoResponse(BaseModel):
    id: int
    vacina_id: int
    dose_numero: int

    class Config:
        from_attributes = True
