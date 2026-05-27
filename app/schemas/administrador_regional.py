from pydantic import BaseModel, EmailStr


class AdminRegionalCreate(BaseModel):
    nome: str
    cpf: str
    email: EmailStr
    telefone: str
    regiao_id: int
    senha: str


class AdminRegionalResponse(BaseModel):
    id: str
    nome: str
    email: EmailStr
    regiao_id: int

    class Config:
        from_attributes = True
