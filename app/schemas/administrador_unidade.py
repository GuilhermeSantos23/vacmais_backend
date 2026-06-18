from uuid import UUID

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
    id: UUID
    nome: str
    cpf: str
    email: str
    telefone: str
    unidade_id: int
    status_conta: str

    class Config:
        from_attributes = True
