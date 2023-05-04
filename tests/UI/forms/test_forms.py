import allure

from pages.forms.page_form import PageForms
from user_generator.person import Person


@allure.epic("Ui tests")
@allure.feature("Forms")
@allure.link(name="Practice Form", url="https://demoqa.com/automation-practice-form")
@allure.title("Тестирование автоматического заполнения формы")
def test_forms(get_driver):
    _user = Person()
    _steps = PageForms(get_driver)
    _steps.step_1_transition()
    _steps.step_2_input_first_name(_user.name)
    _steps.step_3_input_last_name(_user.last_name)
    _steps.step_4_input_user_email(_user.email)
    _steps.step_5_input_gender(_user.gender)
    _steps.step_6_input_phone(_user.nuber)
    _steps.step_7_date_of_birth(_user.date_of_birth)
    _steps.step_8_input_hobbies(_user.hobbies)
    _steps.step_9_avatar("/home/pavel/PycharmProjects/TestToolsQA_Py/img/foxy.png")
    _steps.step_10_current_address_input(_user.current_address)
    _steps.step_11_click_submit()
    _steps.step_12_click_close()
