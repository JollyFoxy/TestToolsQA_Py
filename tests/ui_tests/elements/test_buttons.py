import allure

from pages.elements.page_buttons import PageButtons


@allure.epic("Ui tests")
@allure.feature("Elements")
@allure.link(name="Buttons", url="https://demoqa.com/buttons")
@allure.title("Тест кнопок")
def test_button(get_driver):
    _steps = PageButtons(get_driver)
    _steps.transition()
    _steps.dinamic_click_button()
    _steps.right_click_button()
    _steps.double_click_button()
