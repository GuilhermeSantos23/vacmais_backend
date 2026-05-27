from pydantic import BaseModel


class LogAcessoSensivelResponse(BaseModel):
    id: int
    profissional_id: str
    motivo_acesso: str

    class Config:
        from_attributes = True
