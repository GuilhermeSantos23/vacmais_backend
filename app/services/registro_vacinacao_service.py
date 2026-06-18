from sqlalchemy.orm import Session

from app.models.registro_vacinacao import RegistroVacinacao
from app.schemas.registro_vacinacao import RegistroVacinacaoCreate
from app.services.carteira_vacinacao_service import (
    CarteiraVacinacaoService,
)
from app.services.estoque_service import (
    EstoqueService,
)
from app.services.movimentacao_estoque_service import (
    MovimentacaoEstoqueService,
)


class RegistroVacinacaoService:
    @staticmethod
    def registrar_vacina(
        db: Session,
        data: RegistroVacinacaoCreate,
    ):
        carteira = CarteiraVacinacaoService.buscar_por_usuario(
            db,
            data.usuario_id,
        )

        if not carteira:
            carteira = CarteiraVacinacaoService.criar(
                db,
                data.usuario_id,
            )

        registro = RegistroVacinacao(
            carteira_id=carteira.id,
            vacina_id=data.vacina_id,
            dose_numero=data.dose_numero,
            data_aplicacao=data.data_aplicacao,
            profissional_id=data.profissional_id,
            unidade_id=data.unidade_id,
            origem_registro=data.origem_registro,
            observacoes=data.observacoes,
        )

        db.add(registro)

        estoque = EstoqueService.get_by_lote(
            db,
            data.lote_id,
        )

        if estoque:
            EstoqueService.baixar_estoque(
                db,
                estoque,
                1,
            )

        MovimentacaoEstoqueService.criar_saida_vacinacao(
            db=db,
            lote_id=data.lote_id,
            unidade_id=data.unidade_id,
            profissional_id=data.profissional_id,
        )

        db.commit()
        db.refresh(registro)

        return registro

    @staticmethod
    def listar_por_carteira(
        db: Session,
        carteira_id: int,
    ):
        return (
            db.query(RegistroVacinacao)
            .filter(RegistroVacinacao.carteira_id == carteira_id)
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        registro_id: int,
    ):
        return db.get(
            RegistroVacinacao,
            registro_id,
        )
