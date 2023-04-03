import allure

from pages.elements.page_text_box import PageTextBox


@allure.title("Ввод текста в поле")
def test_text_box(get_driver):
    _steps = PageTextBox(get_driver)
    _steps.step_transition()
    _steps.step_input_name("Lelik")
    _steps.step_input_email("lelik@mail.ru")
    _steps.step_input_current_address("st. Ababab 34")
    _steps.step_input_permanent_address("st. Baba 43")
    _steps.step_click_submit()
