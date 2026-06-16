from pydantic import BaseModel


class ProfissionalCreate(BaseModel):
    nome: str
    cpf: str
    email: str
    telefone: str
    registro_conselho: str
    conselho_profissional: str
    senha: str


class ProfissionalUpdate(BaseModel):
    telefone: str | None = None


class ProfissionalResponse(BaseModel):
    id: str
    nome: str
    cpf: str
    email: str
    telefone: str
    registro_conselho: str
    conselho_profissional: str
    validado_profissional: bool

    class Config:
        from_attributes = True
