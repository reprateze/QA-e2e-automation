import pytest

pytestmark = pytest.mark.api

class TestProductsAPI:
    
    def test_get_todos_os_produtos(self, products_api):
        response = products_api.get_all_products()
        body = response.json()

        assert response.status_code == 200
        assert body["responseCode"] == 200
        assert "products" in body
        assert len(body["products"]) > 0

        produto = body["products"][0]

        assert isinstance(produto["id"], int)
        assert isinstance(produto["name"], str)
        assert isinstance(produto["price"], str)
        assert isinstance(produto["brand"], str)
        assert isinstance(produto["category"], dict)


    @pytest.mark.parametrize("termo_busca, status_esperado, total_minimo_esperado", [
        ("tshirt", 200, 1),             
        ("jeans", 200, 1),               
        ("produto_invalido_xyz", 200, 0),
        ("", 200, 0),        
        ("TShIrT", 200, 1),        
        ("   tshirt   ", 200, 0),  
    ])
    def test_post_pesquise_produtos(self, products_api, termo_busca, status_esperado, total_minimo_esperado):
        response = products_api.pesquisa_produto(termo_busca)
        assert response.status_code == status_esperado

        data = response.json()

        assert "products" in data

        assert len(data["products"]) >= total_minimo_esperado, (
            f"Número de produtos inesperado para '{termo_busca}'. "
            f"Esperado: >= {total_minimo_esperado}, "
            f"Retornado: {len(data['products'])}"
        )
        

    def test_post_todos_produtos(self, products_api):
        response = products_api.post_all_products_list()

        assert response.status_code == 405

        body = response.json()

        assert body["responseCode"] == 405
        assert body ["message"] == "This request method is not supported."