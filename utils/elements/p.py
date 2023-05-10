from selenium.webdriver.chrome.webdriver import WebDriver

from utils.elements.base_element import BaseElement


class P(BaseElement):
    def __init__(self, id: str, driver: WebDriver):
        xpath = f"//p[@id='{id}']"
        super().__init__(xpath, driver)

    def check_text_p(self, text):
        assert self._element.text == text
