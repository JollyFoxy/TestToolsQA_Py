import allure

from api_steps.base_api import BaseApi


class GetNotFoundUser(BaseApi):
    @allure.step("Отправить get запрос пользователя по URL(https://reqres.in/api/users/23)")
    def step_get_not_found_user(self, url: str):
        response = self._requests.get(url)
        assert response.status_code == 404
