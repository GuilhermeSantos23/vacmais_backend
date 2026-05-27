from pydantic import BaseModel, EmailStr


class AdminUnidadeCreate(BaseModel):
    nome: str
    cpf: str
    email: EmailStr
    telefone: str
    unidade_id: int
    senha: str


class AdminUnidadeResponse(BaseModel):
    id: str
    nome: str
    email: EmailStr
    unidade_id: int

    class Config:
        from_attributes = True
