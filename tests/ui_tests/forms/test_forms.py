import os.path

import allure

from pages.forms.page_form import PageForms
from user_generator.user import Person


@allure.epic("Ui tests")
@allure.feature("Forms")
@allure.link(name="Practice Form", url="https://demoqa.com/automation-practice-form")
@allure.title("Тестирование автоматического заполнения формы")
def test_forms(get_driver):
    _user = Person()
    _steps = PageForms(get_driver)
    _steps.transition()
    _steps.input_first_name(_user.name)
    _steps.input_last_name(_user.last_name)
    _steps.input_user_email(_user.email)
    _steps.input_gender(_user.gender)
    _steps.input_phone(_user.nuber)
    _steps.date_of_birth(_user.date_of_birth)
    _steps.input_hobbies(_user.hobbies)
    _steps.avatar("/home/pavel/PycharmProjects/TestToolsQA_Py/img/foxy.png")
    _steps.current_address_input(_user.current_address)
    _steps.click_submit()
    _steps.click_close()
