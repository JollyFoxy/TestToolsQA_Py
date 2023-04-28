import allure

from pages.elements.page_web_tables import PageWebTables


@allure.title("Тест заполнения таблицы")
def test_web_tables(get_driver):
    _steps = PageWebTables(get_driver)
    _steps.step_1_transition()
    _steps.step_2_press_button_add()
    _steps.step_3_input_name("fasdfdsf")
    _steps.step_4_input_last_name("vedvn")
    _steps.step_7_input_salary("griogb")
    _steps.step_8_input_department("mioevmi")
    _steps.step_9_press_button_submit()
