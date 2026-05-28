from fastapi import APIRouter


router = APIRouter(
    prefix="/movimentacao-estoque",
    tags=["Movimentação Estoque"],
)