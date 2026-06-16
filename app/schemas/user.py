from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class UserCreate(BaseModel):
    nome: str
    cpf: str
    email: str
    telefone: str
    sexo: str
    senha: str
    data_nascimento: datetime
    cartao_sus: str | None = None


class UserUpdate(BaseModel):
    nome: str | None = None
    telefone: str | None = None
    sexo: str | None = None
    cartao_sus: str | None = None


class UserResponse(BaseModel):
    id: UUID
    nome: str
    cpf: str
    email: str
    telefone: str
    sexo: str
    cartao_sus: str | None
    ativo: bool

    class Config:
        from_attributes = True
