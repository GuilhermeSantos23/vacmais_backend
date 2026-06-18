from datetime import datetime

from pydantic import BaseModel


class LoteVacinaCreate(BaseModel):
    vacina_id: int
    lote: str
    fabricante: str
    data_validade: datetime


class LoteVacinaResponse(BaseModel):
    id: int
    vacina_id: int
    lote: str
    fabricante: str
    data_validade: datetime

    class Config:
        from_attributes = True
