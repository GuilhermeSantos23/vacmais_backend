from pydantic import BaseModel


class UnidadeCreate(BaseModel):
    nome: str
    tipo: str
    endereco: str
    cidade: str
    estado: str
    telefone: str
    email: str
    latitude: float
    longitude: float
    regiao_id: int


class UnidadeResponse(BaseModel):
    id: int
    nome: str
    tipo: str
    endereco: str
    cidade: str
    estado: str
    telefone: str
    email: str
    latitude: float
    longitude: float
    regiao_id: int

    class Config:
        from_attributes = True
