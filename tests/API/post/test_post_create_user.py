import allure

from api_steps.post.steps_post_create_user import StepsPostCreateUser


@allure.epic("API tests")
@allure.feature("Post")
@allure.title("Создание пользователя")
def test_post_create_user(api_requests):
    StepsPostCreateUser(api_requests).post_create_user("/users")
