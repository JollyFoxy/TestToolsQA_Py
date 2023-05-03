import allure

from pages.book_store.page_register import PageRegister
from user_generator.person import Person


@allure.epic("Ui tests")
@allure.feature("BookStoreApplication")
@allure.link(name="Book Store Application", url="https://demoqa.com/register")
@allure.title("Тест регистрации")
def test_register(get_driver):
    _user = Person()
    _steps = PageRegister(get_driver)
    _steps.step_1_transition()
    _steps.step_2_new_user()
    _steps.step_3_input_first_name(_user.name)
    _steps.step_4_input_last_name(_user.last_name)
    _steps.step_5_input_user_name(_user.user_name)
    _steps.step_6_input_password(_user.password)
    _steps.step_7_captcha()
