from fastapi import HTTPException


def require_active_account(
    user,
):
    if not user.ativo:
        raise HTTPException(
            status_code=403,
            detail="Conta desativada",
        )

    return True
