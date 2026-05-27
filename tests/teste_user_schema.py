from app.schemas.user import UserCreate, UserLogin


def test_user_create_schema():
    user = UserCreate(
        nome="Guilherme",
        cpf="12345678900",
        email="gui@gmail.com",
        senha="123456",
    )

    assert user.nome == "Guilherme"

    assert user.email == "gui@gmail.com"


def test_user_login_schema():
    login = UserLogin(email="gui@gmail.com", senha="123456")

    assert login.email == "gui@gmail.com"
