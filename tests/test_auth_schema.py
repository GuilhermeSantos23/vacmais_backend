from app.schemas.auth import LoginRequest, TokenResponse


def test_login_request_schema():
    login = LoginRequest(email="gui@gmail.com", senha="123456")

    assert login.email == "gui@gmail.com"


def test_token_response_schema():
    token = TokenResponse(access_token="abc123")

    assert token.token_type == "bearer"
