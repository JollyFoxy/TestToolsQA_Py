from utils.elements.base_element import BaseElement


class Li(BaseElement):
    def __init__(self, xpath, driver):
        super().__init__(xpath, driver)
        self.li = self._element