from datetime import datetime

from pydantic import BaseModel


class LoteVacinaCreate(BaseModel):
    vacina_id: int
    lote: str
    fabricante: str
    data_validade: datetime


class LoteVacinaResponse(BaseModel):
    id: int
    lote: str
    fabricante: str

    class Config:
        from_attributes = True
