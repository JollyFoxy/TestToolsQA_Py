import allure

from api_steps.base_api import BaseApi


class StepsPostLogin(BaseApi):
    @allure.step("Отправить post запрос по URL(https://reqres.in/api/login)")
    def post_login(self, url: str):
        body = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        response = self._requests.post(url, body)
        assert response.status_code == 200

    @allure.step("Отправить post запрос по URL(https://reqres.in/api/login)")
    def post_login_unsuccessful(self, url: str):
        body = {
            "email": "peter@klaven"
        }
        response = self._requests.post(url, body)
        assert response.status_code == 400
