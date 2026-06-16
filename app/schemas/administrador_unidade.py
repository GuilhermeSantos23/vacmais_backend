from pydantic import BaseModel


class AdministradorUnidadeCreate(BaseModel):
    nome: str
    cpf: str
    email: str
    telefone: str
    unidade_id: int
    senha: str


class AdministradorUnidadeUpdate(BaseModel):
    telefone: str | None = None


class AdministradorUnidadeResponse(BaseModel):
    id: str
    nome: str
    cpf: str
    email: str
    telefone: str
    unidade_id: int

    class Config:
        from_attributes = True
