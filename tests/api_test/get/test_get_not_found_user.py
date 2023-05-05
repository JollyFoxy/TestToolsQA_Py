import allure

from api_steps.get.steps_get_not_found_user import GetNotFoundUser


@allure.epic("API tests")
@allure.feature("Get")
@allure.title("Получение несуществующего пользователя")
def test_get_not_found_user(api_requests):
    GetNotFoundUser(api_requests).step_get_not_found_user("/users/23")
