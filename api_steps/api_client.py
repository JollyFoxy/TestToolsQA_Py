import allure
import requests


class ApiClient:
    def __init__(self, base_path):
        self.base_path = base_path

    def get(self, path: str = "/"):
        url = f"{self.base_path}{path}"
        return requests.get(url=url)

    def post(self, path: str = "/", json=None):
        url = f"{self.base_path}{path}"
        return requests.post(url=url, json=json)

    def put(self, path: str = "/", json=None):
        url = f"{self.base_path}{path}"
        return requests.put(url=url, json=json)

    def delete(self, path: str = "/"):
        url = f"{self.base_path}{path}"
        return requests.delete(url=url)

    def patch(self, path: str = "/", json=None):
        url = f"{self.base_path}{path}"
        return requests.patch(url=url, json=json)
