import pytest

from tests.API.schemas.brands_schema import BrandsListResponse

pytestmark = pytest.mark.api


class TestBrandsAPI:
    def test_buscar_todas_marcas(self, brands_api):
        response = brands_api.buscar_todas_marcas()
        body = response.json()

        assert response.status_code == 200
        assert body["responseCode"] == 200
        assert "brands" in body
        assert len(body["brands"]) > 0

        BrandsListResponse.model_validate(body)

    def test_atualizar_todas_marcas(self, brands_api):
        response = brands_api.atualizar_todas_marcas()
        body = response.json()

        # Valida que o protocolo web retorna 200
        assert response.status_code == 200

        # Valida que a regra de negócio da API retornou "405" no corpo
        assert body["responseCode"] == 405
        assert body["message"] == "This request method is not supported."

        # Ou seja: o protocolo HTTP deu sucesso (200),
        # mas a regra de negócio da aplicação indicou erro (405).
