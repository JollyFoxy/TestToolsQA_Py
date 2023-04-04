from elements.base_element import BaseElement


class Scrolling(BaseElement):
    def __init__(self, xpath, driver):
        super().__init__(xpath, driver)

    def scroll_to_element(self):
        self._actions.scroll_to_element(self._element).perform()
