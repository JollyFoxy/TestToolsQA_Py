import allure

from api_steps.patch.steps_patch_update_user import StepsPatchUpdateUser


@allure.epic("API tests")
@allure.feature("Patch")
@allure.title("Обновление пользователя")
def test_patch_update_user(api_requests):
    StepsPatchUpdateUser(api_requests).update_user("/users/2")
