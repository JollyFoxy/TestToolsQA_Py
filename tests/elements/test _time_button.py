import allure

from pages.elements.page_time_button import PageTimeButton


@allure.title("Тест ожидания")
def test_time_button(get_driver):
    _steps = PageTimeButton(get_driver)
    _steps.step_transition()
    _steps.step_timeout_button()
