import string

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class BaseElement:
    def __init__(self, xpath, driver):
        self.__driver = driver
        self._element = driver.find_element(By.XPATH, xpath)
        self.__actions = ActionChains(self.__driver)

    def get_text(self) -> str:
        value = self._element.text()
        return value

    def is_visible(self):
        self._element.is_displayed()
