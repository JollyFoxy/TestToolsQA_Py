import allure

from pages.elements.page_web_tables import PageWebTables
from user_generator.user import Person


@allure.epic("Ui tests")
@allure.feature("Elements")
@allure.link(name="Web Tables", url="https://demoqa.com/webtables")
@allure.title("Тест заполнения таблицы")
def test_web_tables(get_driver):
    _user = Person()
    _steps = PageWebTables(get_driver)
    _steps.transition()
    _steps.press_button_add()
    _steps.input_name(_user.name)
    _steps.input_last_name(_user.last_name)
    _steps.input_salary(_user.salary)
    _steps.input_department(_user.department)
    _steps.press_button_submit()
