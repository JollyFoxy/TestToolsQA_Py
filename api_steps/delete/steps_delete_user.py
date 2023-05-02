import allure

from api_steps.base_api import BaseApi


class StepsDeleteUser(BaseApi):
    @allure.step("Отправить delete запрос по URL(https://reqres.in/api/users/2)")
    def delete_user(self, url: str):
        response = self._requests.delete(url)
        assert response.status_code == 204
