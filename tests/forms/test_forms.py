import time

import allure

from pages.forms.page_form import PageForms


@allure.title("")
def test_forms(get_driver):
    _steps = PageForms(get_driver)
    _steps.step_1_transition()
    _steps.step_2_input_first_name("Igor")
    _steps.step_3_input_last_name("Abramov")
    _steps.step_4_input_user_email("igorek@mail.ru")
    _steps.step_5_input_gender("hsdbhv")
    _steps.step_6_input_phone("88005553535")
    _steps.step_7_date_of_birth("11.18.2002")
    _steps.step_8_input_hobbies("Reading", "Sports")
    time.sleep(10)