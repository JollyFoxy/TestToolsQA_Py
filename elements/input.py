from selenium.webdriver import Keys

from elements.base_element import BaseElement


class Input(BaseElement):
    def __init__(self, xpath, driver):
        super().__init__(xpath, driver)
        self.__input = self.__element

    def click_to_input(self):
        self.__input.click()

    def val_input(self, value):
        self.__input.send_keys(value)

    def press_enter_input(self):
        self.__input.send_keys(Keys.ENTER)

    def press_back_space_input(self):
        self.__input.send_keys(Keys.BACK_SPACE)
