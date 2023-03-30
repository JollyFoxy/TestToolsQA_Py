from elements.base_element import BaseElement


class Span(BaseElement):
    def __init__(self, xpath, driver):
        super().__init__(xpath, driver)
        self.__span = self.__element

    def check_text_span(self, text):
        assert self.__span.text() == text
