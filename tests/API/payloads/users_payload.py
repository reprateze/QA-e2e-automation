import time


def gerar_payload_usuario_teste():
    email_unico = f"renan.teste.{int(time.time())}@example.com"
    return {"name": "Renan Teste",
        "email": email_unico,
        "password": "SenhaForte123",
        "title": "Mr",
        "birth_date": "15",
        "birth_month": "6",
        "birth_year": "1995",
        "firstname": "Renan",
        "lastname": "Teste",
        "company": "QA Corp",
        "address1": "Rua Teste, 123",
        "address2": "Apto 45",
        "country": "Brazil",
        "zipcode": "12345-678",
        "state": "Minas Gerais",
        "city": "Santa Rita do Sapucai",
        "mobile_number": "11999998888"
    }