import pytest

from tests.API.schemas.users_schema import MessageResponse, UserDetailsResponse

pytestmark = pytest.mark.api


class TestUsersAPI:
    @pytest.mark.smoke
    def test_criar_conta(self, users_api, dados_usuario_teste):
        response = users_api.criar_conta(dados_usuario_teste)
        body = response.json()

        assert response.status_code == 200
        assert body["responseCode"] == 201
        assert body["message"] == "User created!"
        MessageResponse.model_validate(body)

        users_api.deletar_conta(
            dados_usuario_teste["email"], dados_usuario_teste["password"]
        )

    @pytest.mark.smoke
    def test_login_valido(self, users_api, usuario_criado):
        response = users_api.verificar_login(
            usuario_criado["email"], usuario_criado["password"]
        )
        body = response.json()

        assert response.status_code == 200
        assert body["responseCode"] == 200
        assert body["message"] == "User exists!"
        MessageResponse.model_validate(body)

    @pytest.mark.regression
    def test_login_invalido(self, users_api):
        response = users_api.verificar_login_sem_email("OIIIIIII")
        body = response.json()

        assert response.status_code == 200
        assert body["responseCode"] == 400
        assert body["message"] == "Bad request, email or password parameter is missing in POST request."
        MessageResponse.model_validate(body)

    @pytest.mark.regression
    def test_atualizar_conta(self, users_api, usuario_criado):
        dados_atualizados = usuario_criado.copy()
        dados_atualizados["name"] = "Renan Atualizado"
        dados_atualizados["company"] = "Renan QA Company"

        response = users_api.atualizar_conta(dados_atualizados)
        body = response.json()

        assert response.status_code == 200
        assert body["responseCode"] == 200
        assert body["message"] == "User updated!"
        MessageResponse.model_validate(body)

    @pytest.mark.regression
    def test_buscar_por_email(self, users_api, usuario_criado):
        response = users_api.buscar_por_email(usuario_criado["email"])
        body = response.json()

        assert response.status_code == 200
        assert body["responseCode"] == 200
        assert body["user"]["email"] == usuario_criado["email"]
        UserDetailsResponse.model_validate(body)

    @pytest.mark.regression
    def test_deletar_user(self, users_api, dados_usuario_teste):
        users_api.criar_conta(dados_usuario_teste)

        response = users_api.deletar_conta(
            dados_usuario_teste["email"], dados_usuario_teste["password"]
        )

        body = response.json()

        assert response.status_code == 200
        assert body["responseCode"] == 200
        assert body["message"] == "Account deleted!"
        MessageResponse.model_validate(body)

        response_busca = users_api.buscar_por_email(dados_usuario_teste["email"])

        body_busca = response_busca.json()

        assert body_busca["responseCode"] == 404
        assert body_busca["message"] == "Account not found with this email, try another email!"
        MessageResponse.model_validate(body_busca)
