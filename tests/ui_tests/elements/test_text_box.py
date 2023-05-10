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
    _steps.transition()
    _steps.input_name(_user.name)
    _steps.input_email(_user.email)
    _steps.input_current_address(_user.current_address)
    _steps.input_permanent_address(_user.permanent_address)
    _steps.click_submit()
