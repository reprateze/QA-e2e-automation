from tests.API.clients.base_client import BaseClient


class UsersAPI(BaseClient):


    def criar_conta(self,dados_usuario):
        return self.post("/createAccount", data=dados_usuario)

    def deletar_conta(self,email, senha):
        return self.delete("/deleteAccount",data= {"email":email,"password": senha})

    def verificar_login(self, email, senha):
        return self.post("/verifyLogin", data={"email": email, "password": senha})

    def verificar_login_sem_email(self, senha):
        return self.post(
            "/verifyLogin",
            data={"password": senha}
        )

    def deletar_verificar_login(self):
        return self.delete("/verifyLogin")

    def atualizar_conta(self, dados_usuario):
        return self.put("/updateAccount", data=dados_usuario)

    def buscar_por_email(self,email):
        return self.get("/getUserDetailByEmail", params={"email": email})