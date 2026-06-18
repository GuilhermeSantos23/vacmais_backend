from sqlalchemy.orm import Session

from app.models.log_geral import LogGeral


class LogGeralService:
    @staticmethod
    def registrar(
        db: Session,
        dados: LogGeral,
    ):
        log = LogGeral(**dados.model_dump())

        db.add(log)
        db.commit()
        db.refresh(log)

        return log
