from selenium.webdriver import Keys

from utils.elements.base_element import BaseElement


class Input(BaseElement):
    def __init__(self, xpath, driver):
        super().__init__(xpath, driver)

    def click_to_input(self):
        self._element.click()

    def val_input(self, value):
        self._element.send_keys(value)

    def press_enter_input(self):
        self._element.send_keys(Keys.ENTER)

    def press_back_space_input(self):
        self._element.send_keys(Keys.BACK_SPACE)