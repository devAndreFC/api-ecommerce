import requests


class TestCategorias:
    url_base_categorias = 'http://127.0.0.1:8000/api/v1/categorias/'
    url_refresh = 'http://127.0.0.1:8000/token/refresh/'
    token = {"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4OTA4MDI2NiwiaWF0IjoxNjg4OTkzODY2LCJqdGkiOiI3M2UyOTY1Y2FkYjg0ZGMyODU3ODY4ODZhN2Q3NmY1YSIsInVzZXJfaWQiOjF9.0gQsYgCUGYDMAMZfFPvn4RKw9_h3R3HJVYLH7XBoZ2Q"}
    resposta_refresh = requests.post(url=url_refresh, data=token)
    refresh = resposta_refresh.json()['access']
    headers = {"Authorization": f"Bearer {refresh}"}

    def test_get_categorias(self):
        resposta = requests.get(url=self.url_base_categorias)

        assert resposta.status_code == 200

    def test_get_categoria(self):
        resposta = requests.get(url=f'{self.url_base_categorias}2/')        

        assert resposta.status_code == 200

    def test_post_categoria(self):
        novo = {
            "name": "Promoção"
        }
        
        resposta = requests.post(
            url=self.url_base_categorias,
            headers=self.headders,
            data=novo
        )

        assert resposta.status_code == 201
    
    def test_put_categoria(self):
        att= {
            "name": "Promoção att"
        }
        
        resposta = requests.put(
        url=f'{self.url_base_categorias}10/',
        headers=self.headers,
        data=att
        )

        assert resposta.status_code == 200

    def test_delete_categoria(self):
        resposta = requests.delete(
            url=f'{self.url_base_categorias}9/',
            headers=self.headers
            )
        
        assert resposta.status_code == 204 and len(resposta.text) == 0        
