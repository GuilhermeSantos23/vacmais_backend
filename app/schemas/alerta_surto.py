from pydantic import BaseModel


class AlertaSurtoCreate(BaseModel):
    doenca: str
    descricao: str
    nivel: str


class AlertaSurtoResponse(BaseModel):
    id: int
    doenca: str
    nivel: str

    class Config:
        from_attributes = True
