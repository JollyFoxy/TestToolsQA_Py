import allure

from pages.book_store.page_login import PageLogin
from pages.page_base import BasePage
from utils.elements.input import Input


class PageRegister(BasePage):

    @allure.step("")
    def step_1_transition(self):
        PageLogin(self._driver).transition()

    @allure.step("")
    def step_2_new_user(self):
        PageLogin(self._driver).new_user()

    @allure.step("")
    def step_3_input_first_name(self, name: str):
        first_name = Input("//input[@id='firstname']", self._driver)
        first_name.val_input(name)

    @allure.step("")
    def step_4_input_last_name(self, name: str):
        last_name = Input("//input[@id='lastname']", self._driver)
        last_name.val_input(name)

    @allure.step("")
    def step_5_input_user_name(self, name: str):
        user_name = Input("//input[@id='userName']", self._driver)
        user_name.val_input(name)

    @allure.step("")
    def step_6_input_password(self, pas: str):
        password = Input("//input[@id='password']", self._driver)
        password.val_input(pas)

    @allure.step("")
    def step_7_captcha(self):
        self._captcha_click()
