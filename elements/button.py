from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from elements.base_element import BaseElement


class Button(BaseElement):
    def __init__(self, xpath, driver):
        super().__init__(self, xpath=xpath, driver=driver)
        self.__button = self.__element
        self.__actions = ActionChains(self.__driver)

    def click_button(self):
        self.__button.click()

    def right_click_button(self):
        self.__actions.context_click(self.__button).perform()

    def double_click_button(self):
        self.__actions.double_click(self.__button).perform()
