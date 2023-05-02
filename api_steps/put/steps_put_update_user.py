import allure

from api_steps.base_api import BaseApi


class StepsPutUpdateUser(BaseApi):

    @allure.step("Отправить put запрос по URL(https://reqres.in/api/users/2)")
    def update_user(self, url):
        body = {
            "name": "morpheus",
            "job": "zion resident"
        }
        response = self._requests.put(url, body)
        assert response.status_code == 200
