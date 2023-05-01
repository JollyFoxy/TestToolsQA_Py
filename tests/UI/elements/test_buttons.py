import allure

from pages.elements.page_buttons import PageButtons


@allure.epic("Ui tests")
@allure.feature("Elements")
@allure.link(name="Buttons", url="https://demoqa.com/buttons")
@allure.title("Тест кнопок")
def test_button(get_driver):
    _steps = PageButtons(get_driver)
    _steps.step_1_transition()
    _steps.step_2_dinamic_click_button()
    _steps.step_3_right_click_button()
    _steps.step_4_double_click_button()
