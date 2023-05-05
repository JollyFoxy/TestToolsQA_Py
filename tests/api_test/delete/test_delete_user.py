import allure

from api_steps.delete.steps_delete_user import StepsDeleteUser


@allure.epic("API tests")
@allure.feature("Delete")
@allure.title("Удаление пользователя")
def test_delete_user(api_requests):
    StepsDeleteUser(api_requests).delete_user("/users/2")
