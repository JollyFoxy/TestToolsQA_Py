import allure

from pages.elements.page_buttons import PageButtons


@allure.title("Тест кнопок")
def test_button(get_driver):
    _steps = PageButtons(get_driver)
    _steps.step_transition()
    _steps.step_dinamic_click_button()
    _steps.step_right_click_button()
    _steps.step_double_click_button()
