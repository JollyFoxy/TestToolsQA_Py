import allure

from api_steps.post.authorization.steps_post_register import StepsPostRegister


@allure.epic("API tests")
@allure.feature("Post")
@allure.story("Регистрация")
class TestsRegister:
    @allure.title("Тест регистрации(Позитивный)")
    def test_post_login(self, api_requests):
        StepsPostRegister(api_requests).post_register("/register")

    @allure.title("Тест регистрации(Негативный)")
    def test_post_login_unsuccessful(self, api_requests):
        StepsPostRegister(api_requests).post_register_unsuccessful("/register")
