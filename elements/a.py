from elements.base_element import BaseElement


class A(BaseElement):
    def __init__(self, xpath, driver):
        super().__init__(xpath, driver)

    def hover_to_a(self):
        self.__actions.move_to_element(self._element).perform()

    def click_to_a(self):
        self._element.click()
