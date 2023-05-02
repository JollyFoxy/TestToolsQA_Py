import allure

from api_steps.get.steps_get_user_list import StepsGetUserList


@allure.epic("API tests")
@allure.feature("Get")
@allure.title("Получение списка пользователей")
def test_get_single_user(api_requests):
    StepsGetUserList(api_requests).step_get_user_list("/users?page=2")
