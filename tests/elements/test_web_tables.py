import allure

from pages.elements.page_web_tables import PageWebTables


@allure.title("")
def test_web_tables(get_driver):
    _steps = PageWebTables(get_driver)
    _steps.step_1()
    _steps.step_2()
    _steps.step_3("fasdfdsf")
    _steps.step_4("vedvn")
    _steps.step_7("griogb")
    _steps.step_8("mioevmi")
    _steps.step_9()
