from fastapi import FastAPI

from app.routes.auth import router as auth_router
from app.routes.user import router as users_router
from app.routes.profissional import (
    router as profissionais_router,
)

from app.routes.administrador_unidade import (
    router as admin_unidade_router,
)

from app.routes.administrador_regional import (
    router as admin_regional_router,
)

from app.routes.vacina import (
    router as vacinas_router,
)

from app.routes.registro_vacinacao import (
    router as registros_router,
)

app = FastAPI(title="Vac+ API")


@app.get("/")
def root():
    return {"message": "API está online"}

app.include_router(auth_router)

app.include_router(users_router)

app.include_router(profissionais_router)

app.include_router(admin_unidade_router)

app.include_router(admin_regional_router)

app.include_router(vacinas_router)

app.include_router(registros_router)