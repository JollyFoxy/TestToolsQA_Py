import allure

from api_steps.base_api import BaseApi


class StepsPostRegister(BaseApi):
    @allure.step("Отправить post запрос по URL(https://reqres.in/api/register)")
    def post_register(self, url: str):
        body = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        response = self._requests.post(url, body)
        assert response.status_code == 200

    @allure.step("Отправить post запрос по URL(https://reqres.in/api/register)")
    def post_register_unsuccessful(self, url: str):
        body = {
            "email": "eve.holt@reqres.in",
        }
        response = self._requests.post(url, body)
        assert response.status_code == 400
