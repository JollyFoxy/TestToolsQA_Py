import string

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class BaseElement:
    def __init__(self, xpath, driver):
        self._driver = driver
        self._element = driver.find_element(By.XPATH, xpath)
        self._actions = ActionChains(self._driver)

    def get_text(self):
        value = self._element.text
        return value

    def is_visible(self):
        self._element.is_displayed()

    def is_enabled(self):
        self._element.is_enabled()

    def get_element(self):
        return self._element
