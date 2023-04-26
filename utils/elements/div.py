from selenium.webdriver.chrome.webdriver import WebDriver

from utils.elements.base_element import BaseElement


class Div(BaseElement):
    def __init__(self, xpath: str, driver: WebDriver):
        super().__init__(xpath, driver)

    def drag_and_drop_div(self, element):
        self._actions.drag_and_drop(self._element, element).perform()
