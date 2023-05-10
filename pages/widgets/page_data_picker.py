import time

import allure
from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.page_base import BasePage
from utils.elements.input import Input


class PageDatePicker(BasePage):

    @allure.step("")
    def transition(self):
        self._all_transition("Widgets", "Date Picker")

    @allure.step("")
    def input_date_and_time(self, date_time: str, ec: str):
        input_date_time = Input("dateAndTimePickerInput", self._driver)

        input_date_time.clear_input()
        input_date_time.val_input(date_time)
        input_date_time.press_enter_input()

        assert input_date_time.get_value() == ec
