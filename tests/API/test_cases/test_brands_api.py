import pytest

pytestmark = pytest.mark.api

class TestBrandsAPI:

    def test_get_todas_marcas(self, brands_api):
        response = brands_api.get_todas_marcas()
        body = response.json()

        assert response.status_code == 200
        assert body["responseCode"] == 200
        assert "brands" in body
        assert len(body["brands"]) > 0

        brand = body["brands"][0]
        assert "id" in brand
        assert "brand" in brand
        assert isinstance(brand["id"], int)
        assert isinstance(brand["brand"], str)


    def test_put_todas_marcas(self, brands_api):
       def test_put_todas_marcas(self, brands_api):
        response = brands_api.put_todas_marcas()
        body = response.json()

        # Valida que o protocolo web retorna 200 
        assert response.status_code == 200
        
        # Valida que a regra de negócio da API mandou o "405" no body
        assert body["responseCode"] == 405
        assert body["message"] == "This request method is not supported."

        #Basicamente, o protocolo web deu sucesso (200), mas a regra de negócio da aplicação deu erro (405).

        