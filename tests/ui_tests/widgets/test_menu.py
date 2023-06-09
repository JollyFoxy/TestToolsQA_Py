import allure

from pages.widgets.page_menu import PageMenu


@allure.epic("Ui tests")
@allure.feature("Widgets")
@allure.link(name="Menu", url="https://demoqa.com/menu")
@allure.title("Тест навидения на элименты меню")
def test_menu(get_driver):
    _steps = PageMenu(get_driver)
    _steps.transition()
    _steps.hover_to_element_menu("Main Item 2")
    _steps.hover_to_element_menu("SUB SUB LIST »")
    _steps.hover_to_element_menu("Sub Sub Item 2")
