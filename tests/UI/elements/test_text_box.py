import allure

from pages.elements.page_text_box import PageTextBox


@allure.epic("Ui tests")
@allure.feature("Elements")
@allure.link(name="Text Box", url="https://demoqa.com/text-box")
@allure.title("Ввод текста в поле")
def test_text_box(get_driver):
    _steps = PageTextBox(get_driver)
    _steps.step_1_transition()
    _steps.step_2_input_name("Lelik")
    _steps.step_3_input_email("lelik@mail.ru")
    _steps.step_4_input_current_address("st. Ababab 34")
    _steps.step_5_input_permanent_address("st. Baba 43")
    _steps.step_6_click_submit()
