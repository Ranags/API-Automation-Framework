import requests

class APIS:
    BASE_URL = "Https://jsonplaceholder.typicode.com"

    def __init__(self):
        self.header = {

            "Content-Type":"Application/json"
        }

    def get(self,endpoint):
        url=f'{self.BASE_URL}/{endpoint}'
        response=requests.get(url,headers=self.header)
        return response



    def post(self,endpoint,data):
        url=f'{self.BASE_URL}/{endpoint}'
        response=requests.post(url,headers=self.header,json=data)
        return response