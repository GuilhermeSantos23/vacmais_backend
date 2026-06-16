from pydantic import BaseModel


class VacinaCreate(BaseModel):
    nome: str
    descricao: str
    doses_necessarias: int
    intervalo_dias: int
    faixa_etaria_min: int
    faixa_etaria_max: int
    obrigatoria: bool


class VacinaUpdate(BaseModel):
    nome: str | None = None
    descricao: str | None = None
    doses_necessarias: int | None = None
    intervalo_dias: int | None = None
    faixa_etaria_min: int | None = None
    faixa_etaria_max: int | None = None
    obrigatoria: bool | None = None


class VacinaResponse(BaseModel):
    id: int
    nome: str

    class Config:
        from_attributes = True
