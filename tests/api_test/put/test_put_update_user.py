import allure

from api_steps.put.steps_put_update_user import StepsPutUpdateUser


@allure.epic("API tests")
@allure.feature("Put")
@allure.title("Обновление пользователя")
def test_put_update_user(api_requests):
    StepsPutUpdateUser(api_requests).update_user("/users/2")
