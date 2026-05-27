from pydantic import BaseModel


class CondicaoSensivelCreate(BaseModel):
    cidadao_id: str
    tipo_condicao: str
    descricao: str


class CondicaoSensivelResponse(BaseModel):
    id: int
    tipo_condicao: str
    descricao: str

    class Config:
        from_attributes = True
