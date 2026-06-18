from pydantic import BaseModel


class InformativoSaudeCreate(BaseModel):
    titulo: str
    conteudo: str
    tipo: str
    autor_id: str


class InformativoSaudeResponse(BaseModel):
    id: int
    titulo: str
    tipo: str

    class Config:
        from_attributes = True
