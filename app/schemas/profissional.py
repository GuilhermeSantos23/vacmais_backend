from pydantic import BaseModel, EmailStr


class ProfissionalCreate(BaseModel):
    nome: str
    cpf: str
    email: EmailStr
    telefone: str
    registro_conselho: str
    conselho_profissional: str
    senha: str


class ProfissionalResponse(BaseModel):
    id: str
    nome: str
    email: EmailStr
    conselho_profissional: str

    class Config:
        from_attributes = True
