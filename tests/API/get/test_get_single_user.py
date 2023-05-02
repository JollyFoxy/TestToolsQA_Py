import allure

from api_steps.get.steps_get_single_user import StepsGetSingleUser


@allure.epic("API tests")
@allure.feature("Get")
@allure.title("Получение одного пользователя")
def test_get_single_user(api_requests):
    StepsGetSingleUser(api_requests).step_get_single_user("/users/2")

