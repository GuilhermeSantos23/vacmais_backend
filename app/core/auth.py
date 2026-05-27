from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from app.utils.security import decode_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)

    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido")

    return payload


def get_current_profissional(user=Depends(get_current_user)):
    if user["tipo"] != "profissional":
        raise HTTPException(status_code=403, detail="Acesso negado")

    return user


def get_current_admin_regional(user=Depends(get_current_user)):
    if user["tipo"] != "admin_regional":
        raise HTTPException(status_code=403, detail="Acesso negado")

    return user


def get_current_admin_unidade(user=Depends(get_current_user)):
    if user["tipo"] != "admin_unidade":
        raise HTTPException(status_code=403, detail="Acesso negado")

    return user
