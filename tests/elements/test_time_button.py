import allure

from pages.elements.page_time_button import PageTimeButton


@allure.title("Тест ожидания")
def test_time_button(get_driver):
    _steps = PageTimeButton(get_driver)
    _steps.step_1_transition()
    _steps.step_2_timeout_button()
    _steps.step_3_enable_button()
