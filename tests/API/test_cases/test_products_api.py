import pytest

from tests.API.schemas.products_schema import ProductsListResponse

pytestmark = pytest.mark.api


class TestProductsAPI:
    @pytest.mark.smoke
    def test_buscar_todos_os_produtos(self, products_api):
        response = products_api.buscar_todos_produtos()
        body = response.json()

        assert response.status_code == 200
        assert body["responseCode"] == 200
        assert "products" in body
        assert len(body["products"]) > 0

        ProductsListResponse.model_validate(body)

    @pytest.mark.regression
    @pytest.mark.parametrize(
        "termo_busca, resultado_esperado",
        [
            ("tshirt", "encontrado"),
            ("jeans", "encontrado"),
            ("produto_invalido_xyz", "vazio"),
            ("", "encontrado"),  # API retorna todos os produtos quando busca é vazia
            ("TShIrT", "encontrado"),
            ("   tshirt   ", "vazio"),
        ],
    )
    def test_pesquisar_produtos(self, products_api, termo_busca, resultado_esperado):
        response = products_api.pesquisar_produto(termo_busca)
        assert response.status_code == 200

        data = response.json()
        assert "products" in data

        if resultado_esperado == "encontrado":
            assert len(data["products"]) > 0, (
                f"Esperava encontrar produtos para '{termo_busca}', mas veio vazio."
            )
        else:
            assert len(data["products"]) == 0, (
                f"Esperava lista vazia para '{termo_busca}', "
                f"mas retornou {len(data['products'])} produto(s)."
            )

    @pytest.mark.regression
    def test_pesquisar_produtos_sem_parametro(self, products_api):
        response = products_api.pesquisar_produto_sem_parametro()
        data = response.json()

        assert response.status_code == 200
        assert data["responseCode"] == 400
        assert (
            data["message"]
            == "Bad request, search_product parameter is missing in POST request."
        )

    @pytest.mark.regression
    def test_enviar_todos_produtos(self, products_api):
        response = products_api.enviar_todos_produtos()
        body = response.json()

        assert response.status_code == 200
        assert body["responseCode"] == 405
        assert body["message"] == "This request method is not supported."

    @pytest.mark.regression
    def test_pesquisar_produtos_termo_vazio_retorna_todos(self, products_api):
        response = products_api.pesquisar_produto("")
        data = response.json()

        assert response.status_code == 200
        assert len(data["products"]) == 34, (
            "Comportamento conhecido da API: busca vazia retorna o catálogo completo, "
            "não uma lista vazia."
        )
