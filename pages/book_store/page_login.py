import time

from pages.page_base import BasePage
from utils.elements.button import Button
from utils.tools.scroling import Scrolling


class PageLogin(BasePage):
    def transition(self):
        Scrolling(self._driver).scroll_to(y=900)
        self._first_element_transition("Book Store Application")
        Scrolling(self._driver).scroll_to(y=900)
        self._second_element_transition("Login")
    def new_user(self):
        new_user_btn = Button("//button[@id='newUser']", self._driver)
        new_user_btn.click_button()
