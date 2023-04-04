from selenium.webdriver.common.by import By

from elements.button import Button
from pages.page_base import BasePage
from elements.scroling import Scrolling


class PageTimeButton(BasePage):
    def step_transition(self):
        self._first_element_transition("Elements")
        scrolling = Scrolling("//li[@id='item-8']", self._driver)
        scrolling.scroll_to_element()
        self._second_element_transition("Dynamic Properties")

    def step_timeout_button(self):
        timeout_button = Button("visibleAfter", self._driver)
        timeout_button.click_button()
