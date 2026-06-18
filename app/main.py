from fastapi import FastAPI

from app.routes.administrador_regional import (
    router as admin_regional_router,
)
from app.routes.administrador_unidade import (
    router as admin_unidade_router,
)
from app.routes.auth import router as auth_router
from app.routes.campanha_vacinacao import (
    router as campanha_vacinacao_router,
)
from app.routes.carteira_vacinacao import (
    router as carteira_vacinacao_router,
)
from app.routes.estoque import (
    router as estoque_router,
)
from app.routes.informativo_saude import (
    router as informativo_saude_router,
)
from app.routes.lote_vacina import (
    router as lote_vacina_router,
)
from app.routes.movimentacao_estoque import (
    router as movimentacao_estoque_router,
)
from app.routes.profissional import (
    router as profissionais_router,
)
from app.routes.regiao import (
    router as regioes_router,
)
from app.routes.registro_vacinacao import (
    router as registro_vacinacao_router,
)
from app.routes.unidade import (
    router as unidades_router,
)
from app.routes.user import router as users_router
from app.routes.vacina import (
    router as vacinas_router,
)

app = FastAPI(
    title="Vac+ API",
)


@app.get("/")
def root():
    return {
        "message": "API está online",
    }


app.include_router(auth_router)

app.include_router(users_router)

app.include_router(profissionais_router)

app.include_router(admin_unidade_router)

app.include_router(admin_regional_router)

app.include_router(vacinas_router)

app.include_router(regioes_router)

app.include_router(unidades_router)

app.include_router(lote_vacina_router)

app.include_router(estoque_router)

app.include_router(movimentacao_estoque_router)

app.include_router(registro_vacinacao_router)

app.include_router(carteira_vacinacao_router)

app.include_router(campanha_vacinacao_router)

app.include_router(informativo_saude_router)
