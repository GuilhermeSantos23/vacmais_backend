from pydantic import BaseModel


class VacinaCreate(BaseModel):
    nome: str
    descricao: str
    doses_necessarias: int


class VacinaResponse(BaseModel):
    id: int
    nome: str
    descricao: str

    class Config:
        from_attributes = True
