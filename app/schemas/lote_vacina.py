from pydantic import BaseModel


class LoteVacinaCreate(BaseModel):
    vacina_id: int
    lote: str
    fabricante: str


class LoteVacinaResponse(BaseModel):
    id: int
    lote: str
    fabricante: str

    class Config:
        from_attributes = True
