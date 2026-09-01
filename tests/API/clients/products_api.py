from tests.API.clients.base_client import BaseClient


class ProductsAPI(BaseClient):

    def buscar_todos_produtos(self):
        return self.get("/productsList")

    def pesquisar_produto(self, termo_busca):
        return self.post(
            "/searchProduct",
            data={"search_product": termo_busca}
        )

    def enviar_todos_produtos(self):
        return self.post("/productsList")

    def pesquisar_produto_sem_parametro(self):
        return self.post("/searchProduct")