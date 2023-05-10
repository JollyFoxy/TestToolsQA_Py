import allure

from pages.elements.page_time_button import PageTimeButton


@allure.epic("Ui tests")
@allure.feature("Elements")
@allure.link(name="Dynamic Properties", url="https://demoqa.com/dynamic-properties")
@allure.title("Тест ожидания")
def test_time_button(get_driver):
    _steps = PageTimeButton(get_driver)
    _steps.transition()
    _steps.timeout_button()
    _steps.enable_button()
    _steps.color_change_button()
