import allure

from pages.widgets.page_menu import PageMenu


@allure.title("Тест навидения на элименты меню")
def test_menu(get_driver):
    _steps = PageMenu(get_driver)
    _steps.step_1_transition()
    _steps.step_hover_to_element_menu("Main Item 2")
    _steps.step_hover_to_element_menu("SUB SUB LIST »")
    _steps.step_hover_to_element_menu("Sub Sub Item 2")
