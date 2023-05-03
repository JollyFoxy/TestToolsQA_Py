import allure

from pages.elements.page_web_tables import PageWebTables
from user_generator.person import Person


@allure.epic("Ui tests")
@allure.feature("Elements")
@allure.link(name="Web Tables", url="https://demoqa.com/webtables")
@allure.title("Тест заполнения таблицы")
def test_web_tables(get_driver):
    _user = Person()
    _steps = PageWebTables(get_driver)
    _steps.step_1_transition()
    _steps.step_2_press_button_add()
    _steps.step_3_input_name(_user.name)
    _steps.step_4_input_last_name(_user.last_name)
    _steps.step_7_input_salary(_user.salary)
    _steps.step_8_input_department(_user.department)
    _steps.step_9_press_button_submit()
