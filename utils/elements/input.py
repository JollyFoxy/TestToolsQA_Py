from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver

from utils.elements.base_element import BaseElement


class Input(BaseElement):
    def __init__(self, id: str, driver: WebDriver):
        xpath = f"//input[@id='{id}']"
        super().__init__(xpath, driver)

    def click_to_input(self):
        self._element.click()

    def val_input(self, value):
        self._element.send_keys(value)

    def press_enter_input(self):
        self._element.send_keys(Keys.ENTER)

    def press_back_space_input(self):
        self._element.send_keys(Keys.BACK_SPACE)

    def clear_input(self):
        self._element.clear()

    def press_arrow_left_input(self):
        self._element.send_keys(Keys.ARROW_LEFT)

