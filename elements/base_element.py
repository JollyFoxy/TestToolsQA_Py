import string

from selenium.webdriver.common.by import By


class BaseElement:
    def __init__(self, xpath, driver):
        self.__driver = driver
        self.__element = driver.find_element(By.XPATH, xpath)

    def get_text(self) -> string:
        value = self.__element.text()
        return value
