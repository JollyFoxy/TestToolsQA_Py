from selenium.webdriver import ActionChains
from elements.base_element import BaseElement


class Button(BaseElement):
    def __init__(self, xpath, driver):
        super().__init__(xpath, driver)
        self.__button = self.__element

    def click_button(self):
        self.__element.click()

    def right_click_button(self):
        self.__actions.context_click(self.__element).perform()
        self.__actions.context_click(self.__element).perform()

    def double_click_button(self):
        self.__actions.double_click(self.__element).perform()
