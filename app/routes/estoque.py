from fastapi import APIRouter


router = APIRouter(
    prefix="/estoque",
    tags=["Estoque"],
)