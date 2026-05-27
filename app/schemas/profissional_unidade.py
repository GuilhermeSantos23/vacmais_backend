from pydantic import BaseModel


class ProfissionalUnidadeCreate(BaseModel):
    profissional_id: str
    unidade_id: int
    cargo: str


class ProfissionalUnidadeResponse(BaseModel):
    id: int
    cargo: str

    class Config:
        from_attributes = True
