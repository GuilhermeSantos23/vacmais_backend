from http import HTTPStatus


def test_create_user_and_login(client):
    create_response = client.post(
        "/users/",
        json={
            "nome": "Teste testado",
            "cpf": "98765432101",
            "email": "test@email.com",
            "telefone": "11988888888",
            "sexo": "F",
            "cartao_sus": "987654320",
            "senha": "123456",
            "data_nascimento": "1995-05-10T00:00:00",
        },
    )

    assert create_response.status_code == HTTPStatus.CREATED

    login_response = client.post(
        "/auth/login/user",
        json={
            "email": "test@email.com",
            "senha": "123456",
        },
    )

    assert login_response.status_code == HTTPStatus.OK

    data = login_response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"
