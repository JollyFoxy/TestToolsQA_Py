from selenium.webdriver.chrome.webdriver import WebDriver

from utils.elements.base_element import BaseElement


class Button(BaseElement):
    def __init__(self, xpath: str = None, id: str = None, driver: WebDriver = None):
        if xpath is None:
            xpath = f"//button[@id='{id}']"
        super().__init__(xpath, driver)

    def click_button(self):
        self._element.click()

    def right_click_button(self):
        self._actions.context_click(self._element).perform()

    def double_click_button(self):
        self._actions.double_click(self._element).perform()
