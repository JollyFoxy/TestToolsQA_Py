import allure

from api_steps.post.authorization.steps_post_login import StepsPostLogin


@allure.epic("API tests")
@allure.feature("Post")
@allure.story("Авторизация")
class TestsLogin:
    @allure.title("Тест авторизации(Позитивный)")
    def test_post_login(self, api_requests):
        StepsPostLogin(api_requests).post_login("/login")

    @allure.title("Тест авторизации(Негативный)")
    def test_post_login_unsuccessful(self, api_requests):
        StepsPostLogin(api_requests).post_login_unsuccessful("/login")
