from utils.elements.base_element import BaseElement


class Span(BaseElement):
    def __init__(self, xpath, driver):
        super().__init__(xpath, driver)

    def check_text_span(self, text):
        assert self._element.text() == text
