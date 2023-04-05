import time

from pages.page_base import BasePage
from utils.elements.button import Button
from utils.tools.scroling import Scrolling
from utils.tools.waiting import Waiting


class PageTimeButton(BasePage):
    def step_1_transition(self):
        self._first_element_transition("Elements")
        Scrolling(self._driver).scroll_to(y=300)
        self._second_element_transition("Dynamic Properties")

    def step_2_timeout_button(self):
        timeout_button = Button("//button[@id='visibleAfter']", self._driver)
        timeout_button.click_button()
        self._driver.refresh()

    def step_3_enable_button(self):
        no_clickable_button = Button("//button[@id='enableAfter']", self._driver)
        Waiting(self._driver).wait_to_element_clickable(no_clickable_button.get_element())
        self._driver.refresh()

    # def step_4_color_change_button(self):
    #     color_change_button = Button("//button[@id='colorChange']", self._driver).get_element()
    #     Waiting(self._driver).wait_all_of(color_change_button.value_of_css_property("color") == "rgba(22 0, 53, 69, 1)")
    #     self._driver.refresh()
