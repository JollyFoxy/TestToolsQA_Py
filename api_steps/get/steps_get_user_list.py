import allure

from api_steps.base_api import BaseApi


class StepsGetUserList(BaseApi):

    @allure.step("Отправить get запрос списка пользователей по URL(https://reqres.in/api/users?page=2)")
    def step_get_user_list(self, url: str):
        response = self._requests.get(url)
        assert response.status_code == 200
