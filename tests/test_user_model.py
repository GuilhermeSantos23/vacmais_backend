from datetime import datetime

from app.models.user import StatusContaEnum, User


def test_criar_usuario():
    usuario = User(
        nome="Guilherme",
        cpf="12345678900",
        email="gui@gmail.com",
        telefone="98732-0078",
        sexo="M",
        cartao_sus=None,
        senha_hash="123456",
        data_nascimento=datetime.strptime("27/07/2008", "%d/%m/%Y"),
        status_conta=StatusContaEnum.ativo,
    )

    assert usuario.nome == "Guilherme"
