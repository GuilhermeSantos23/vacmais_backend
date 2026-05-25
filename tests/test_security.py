from app.utils.security import (
    create_access_token,
    hash_password,
    verify_password,
    verify_token,
)


def test_hash_password():
    password = "123456"

    hashed = hash_password(password)

    assert hashed != password
    assert isinstance(hashed, str)


def test_verify_password():
    password = "123456"

    hashed = hash_password(password)

    assert verify_password(password, hashed) is True


def test_verify_wrong_password():
    password = "123456"

    hashed = hash_password(password)

    assert verify_password("senha_errada", hashed) is False


def test_create_access_token():
    data = {"sub": "123"}

    token = create_access_token(data)

    assert token is not None
    assert isinstance(token, str)


def test_verify_token():
    data = {"sub": "123"}

    token = create_access_token(data)

    payload = verify_token(token)

    assert payload is not None
    assert payload["sub"] == "123"


def test_verify_invalid_token():
    payload = verify_token("token_invalido")

    assert payload is None
