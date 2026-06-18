from pydantic import BaseModel


class CondicaoVacinaRestritaCreate(BaseModel):
    tipo_condicao: str
    vacina_id: int
    motivo: str | None = None


class CondicaoVacinaRestritaResponse(BaseModel):
    id: int
    tipo_condicao: str
    vacina_id: int
    motivo: str | None = None

    class Config:
        from_attributes = True
