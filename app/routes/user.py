"""
Aqui está a definição dos endpoints da API.

Aqui deve ser desenvolvido :
- A criação de rotas (GET, POST, PUT, DELETE)
- O recebimento de requisições do front-end
- Chamar os services

Exemplo:
@router.post("/usuarios")
"""
from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.auth import get_current_user

from app.database.connection import get_db

from app.schemas.user import (
    UserCreate,
    UserResponse,
)

from app.services.user_service import (
    UserService,
)


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


# =========================
# CREATE USER
# =========================

@router.post(
    "/",
    response_model=UserResponse,
    status_code=HTTPStatus.CREATED,
)
def create_user(
    data: UserCreate,
    db: Session = Depends(get_db),
):

    return UserService.create_user(
        db,
        data,
    )


# =========================
# GET ME
# =========================

@router.get(
    "/me",
    response_model=UserResponse,
)
def get_me(
    user=Depends(get_current_user),
):

    return user


# =========================
# DEACTIVATE USER
# =========================

@router.patch(
    "/deactivate",
    response_model=UserResponse,
)
def deactivate_user(
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):

    return UserService.deactivate_user(
        db,
        user,
    )