from sqlalchemy.orm import Session

from app.models.unidade import Unidade


class UnidadeService:

    @staticmethod
    def create_unidade(
        db: Session,
        data,
    ):

        unidade = Unidade(
            nome=data.nome,
            tipo=data.tipo,
            cidade=data.cidade,
            estado=data.estado,
            endereco=data.endereco,
            telefone=data.telefone,
            email=data.email,
        )

        db.add(unidade)

        db.commit()

        db.refresh(unidade)

        return unidade