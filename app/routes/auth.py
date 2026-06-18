from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.auth import (
    LoginRequest,
    TokenResponse,
)
from app.services.auth_service import (
    AuthService,
)

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post(
    "/login",
    response_model=TokenResponse,
    status_code=HTTPStatus.OK,
)
def login(
    data: LoginRequest,
    db: Session = Depends(get_db),
):
    token = AuthService.authenticate(
        db,
        data.email,
        data.senha,
    )

    if not token:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail="Email ou senha inválidos",
        )

    return token
