from pydantic import BaseModel


class AdministradorRegionalCreate(BaseModel):
    nome: str
    cpf: str
    email: str
    telefone: str
    registro_regional: str
    regiao_id: int
    senha: str


class AdministradorRegionalUpdate(BaseModel):
    telefone: str | None = None


class AdministradorRegionalResponse(BaseModel):
    id: str
    nome: str
    cpf: str
    email: str
    telefone: str
    registro_regional: str
    regiao_id: int

    class Config:
        from_attributes = True
