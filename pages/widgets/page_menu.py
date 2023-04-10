import allure

from pages.page_base import BasePage
from utils.elements.a import A
from utils.tools.scroling import Scrolling


class PageMenu(BasePage):

    @allure.step("")
    def step_1_transition(self):
        self._first_element_transition("Widgets")
        Scrolling(self._driver).scroll_to(y=400)
        self._second_element_transition("Menu")

    @allure.step("")
    def step_2_hover_main_item2(self):
        main_item2 = A("//a[.='Main Item 2']", self._driver)
        main_item2.hover_to_a()
    @allure.step("")
    def step_3_hover_sub_list(self):
        sub_list = A("//a[.='SUB SUB LIST »']", self._driver)
        sub_list.hover_to_a()
    @allure.step("")
    def step_4_hover_sub_sub_item2(self):
        sub_sub_item2 = A("//a[.='Sub Sub Item 2']", self._driver)
        sub_sub_item2.hover_to_a()

