from elements.base_element import BaseElement


class TextArea(BaseElement):
    def __init__(self, xpath, driver):
        super().__init__(xpath, driver)
        self.__text_area = self.__element

    def val_input(self, value):
        self.__text_area.send_keys(value)
