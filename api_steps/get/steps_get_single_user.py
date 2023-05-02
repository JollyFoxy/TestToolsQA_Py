import allure

from api_steps.base_api import BaseApi


class StepsGetSingleUser(BaseApi):
    @allure.step("Отправить get запрос пользователя по URL(https://reqres.in/api/users/2)")
    def step_get_single_user(self, url: str):
        response = self._requests.get(url)
        assert response.status_code == 200
