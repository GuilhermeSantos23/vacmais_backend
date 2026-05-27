from pydantic import BaseModel


class LogGeralResponse(BaseModel):
    id: int
    usuario_tipo: str
    acao: str
    entidade_afetada: str

    class Config:
        from_attributes = True
