from tests.API.clients.base_client import BaseClient

class BrandsAPI(BaseClient):

    def get_todas_marcas(self):
       return self.get("/brandsList")