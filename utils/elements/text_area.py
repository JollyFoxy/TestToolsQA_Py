from utils.elements.base_element import BaseElement


class TextArea(BaseElement):
    def __init__(self, xpath, driver):
        super().__init__(xpath, driver)

    def val_text_area(self, value):
        self._element.send_keys(value)
