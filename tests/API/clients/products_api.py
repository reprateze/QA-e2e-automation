from tests.API.clients.base_client import BaseClient


class ProductsAPI(BaseClient):

    def get_all_products(self):
        return self.get("/productsList")
    
  
    def pesquisa_produto(self, termo_busca):
        return self.post(
            "/searchProduct",
            data={"search_product": termo_busca}
        )

    def post_all_products_list(self):
        return self.post("/productsList")

    def pesquisa_produto_sem_parametro(self):
        return self.post("/searchProduct")
