import allure

from pages.book_store.page_register import PageRegister
from user_generator.user import Person


@allure.epic("Ui tests")
@allure.feature("BookStoreApplication")
@allure.link(name="Book Store Application", url="https://demoqa.com/register")
@allure.title("Тест регистрации")
def test_register(get_driver):
    _user = Person()
    _steps = PageRegister(get_driver)
    _steps.transition()
    _steps.new_user()
    _steps.input_first_name(_user.name)
    _steps.input_last_name(_user.last_name)
    _steps.input_user_name(_user.user_name)
    _steps.input_password(_user.password)
    _steps.captcha()
