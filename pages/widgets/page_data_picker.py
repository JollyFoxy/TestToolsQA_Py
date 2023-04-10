import allure

from pages.page_base import BasePage
from utils.elements.input import Input


class PageDatePicker(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._input_date_time = Input("//input[@id='dateAndTimePickerInput']", self._driver)

    @allure.step("")
    def step_1_transition(self):
        self._all_transition("Widgets", "Date Picker")

    @allure.step("")
    def step_2_input_date_and_time(self, date_time):
        self._input_date_time.clear_input()
        self._input_date_time.val_input(date_time)
        self._input_date_time.press_enter_input()

    def step_3_check_input(self, ec):
        assert self._input_date_time.get_text() == ec