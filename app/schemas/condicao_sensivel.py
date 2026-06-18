from uuid import UUID

from pydantic import BaseModel


class CondicaoSensivelCreate(BaseModel):
    usuario_id: UUID
    profissional_registro_id: UUID
    tipo_condicao: str
    descricao: str


class CondicaoSensivelUpdate(BaseModel):
    descricao: str | None = None


class CondicaoSensivelResponse(BaseModel):
    id: int
    tipo_condicao: str
    descricao: str

    class Config:
        from_attributes = True
