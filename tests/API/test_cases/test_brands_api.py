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

        