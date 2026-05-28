"""
Aqui é onde é feita a validação de dados usando Pydantic.

Aqui deve ser desenvolvido:
- A criação de schemas de entrada (POST, PUT)
- A criação de schemas de saída (resposta da API)
- E a validação de dados antes de chegar no banco

Exemplo:
class UserCreate(BaseModel):
    nome: str
    email: str
"""

from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):

    nome: str
    cpf: str
    email: EmailStr
    telefone: str
    sexo: str
    senha: str
    data_nascimento: datetime
    cartao_sus: str | None = None

class UserLogin(BaseModel):
    email: EmailStr
    senha: str


class UserResponse(BaseModel):
    id: str
    nome: str
    email: EmailStr

    class Config:
        from_attributes = True
