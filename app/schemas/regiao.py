from pydantic import BaseModel


class RegiaoCreate(BaseModel):
    nome: str
    cidade: str
    estado: str


class RegiaoResponse(BaseModel):
    id: int
    nome: str
    cidade: str
    estado: str

    class Config:
        from_attributes = True
