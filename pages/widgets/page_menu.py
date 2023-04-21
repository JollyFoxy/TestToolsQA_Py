import time

import allure

from pages.page_base import BasePage
from utils.elements.a import A
from utils.tools.scroling import Scrolling


class PageMenu(BasePage):

    @allure.step("")
    def step_1_transition(self):
        self._first_element_transition("Widgets")
        Scrolling(self._driver).scroll_to(y="4000")
        self._second_element_transition("Menu")

    @allure.step("")
    def step_hover_to_element_menu(self, element: str):
        el_a = A(f"//a[.='{element}']", self._driver)
        el_a.hover_to_a()
