import allure

from pages.book_store.page_register import PageRegister


@allure.title("")
def test_register(get_driver):
    _steps = PageRegister(get_driver)
    _steps.step_1_transition()
    _steps.step_2_new_user()
    _steps.step_3_input_first_name("Abraham")
    _steps.step_4_input_last_name("Friman")
    _steps.step_5_input_user_name("Loxy")
    _steps.step_6_input_password("Qq-123456!")
    _steps.step_7_captcha()
