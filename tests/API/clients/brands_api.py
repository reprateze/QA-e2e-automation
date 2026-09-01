from tests.API.clients.base_client import BaseClient


class BrandsAPI(BaseClient):

    def buscar_todas_marcas(self):
        return self.get("/brandsList")

    def atualizar_todas_marcas(self):
        return self.put("/brandsList")