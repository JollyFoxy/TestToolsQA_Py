import allure

from pages.elements.page_text_box import PageTextBox
from user_generator.user import Person


@allure.epic("Ui tests")
@allure.feature("Elements")
@allure.link(name="Text Box", url="https://demoqa.com/text-box")
@allure.title("Ввод текста в поле")
def test_text_box(get_driver):
    _user = Person()
    _steps = PageTextBox(get_driver)
    _steps.step_1_transition()
    _steps.step_2_input_name(_user.name)
    _steps.step_3_input_email(_user.email)
    _steps.step_4_input_current_address(_user.current_address)
    _steps.step_5_input_permanent_address(_user.permanent_address)
    _steps.step_6_click_submit()
