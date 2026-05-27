from pydantic import BaseModel


class ProfissionalObrigatoriedadeVacinalCreate(BaseModel):
    profissional_id: str
    vacina_id: int


class ProfissionalObrigatoriedadeVacinalResponse(BaseModel):
    id: int
    profissional_id: str
    vacina_id: int

    class Config:
        from_attributes = True
