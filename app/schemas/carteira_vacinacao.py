from uuid import UUID

from pydantic import BaseModel


class CarteiraVacinacaoCreate(BaseModel):
    usuario_id: UUID


class CarteiraVacinacaoResponse(BaseModel):
    id: int
    usuario_id: UUID

    class Config:
        from_attributes = True
