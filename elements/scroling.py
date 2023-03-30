from elements.base_element import BaseElement


class scrolling(BaseElement):
    def __init__(self, xpath, driver):
        super().__init__(xpath, driver)

    def scroll_to_element(self, element):
        self.__actions.scroll_to_element(element).perform()
