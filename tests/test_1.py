import allure

from pages.page import StepsTest1


@allure.title("Ввод текста в поле")
def test_1(get_driver):
    run1 = StepsTest1(get_driver)
    run1.go_to_site()
    run1.step_transition()
    run1.step_input_name("Lelik")
