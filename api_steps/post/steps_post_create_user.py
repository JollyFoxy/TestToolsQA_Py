import allure

from api_steps.base_api import BaseApi


class StepsPostCreateUser(BaseApi):

    @allure.step("Отправить post запрос по URL(https://reqres.in/api/users)")
    def post_create_user(self, url: str):
        body = {
            "name": "morpheus",
            "job": "leader"
        }
        response = self._requests.post(url, body)
        assert response.status_code == 201
