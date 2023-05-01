import allure

from pages.book_store.page_login import PageLogin
from pages.page_base import BasePage
from utils.elements.button import Button
from utils.elements.input import Input


class PageRegister(BasePage):

    @allure.step("Переход")
    def step_1_transition(self):
        PageLogin(self._driver).transition()

    @allure.step("Нажатие кнопки \"New User\"")
    def step_2_new_user(self):
        PageLogin(self._driver).new_user()

    @allure.step("Ввод в поле \"First Name\"")
    def step_3_input_first_name(self, name: str):
        first_name = Input("//input[@id='firstname']", self._driver)
        first_name.val_input(name)

    @allure.step("Ввод в поле \"Last Name\"")
    def step_4_input_last_name(self, name: str):
        last_name = Input("//input[@id='lastname']", self._driver)
        last_name.val_input(name)

    @allure.step("Ввод в поле \"User Name\"")
    def step_5_input_user_name(self, name: str):
        user_name = Input("//input[@id='userName']", self._driver)
        user_name.val_input(name)

    @allure.step("Ввод в поле \"Password\"")
    def step_6_input_password(self, pas: str):
        password = Input("//input[@id='password']", self._driver)
        password.val_input(pas)

    @allure.step("Нажатие на капчу")
    def step_7_captcha(self):
        self._captcha_click()

    @allure.step("Нажатие на кнопку \"Register\"")
    def step_8_register(self):
        register_btn = Button("//button[@id='register']", self._driver)
        register_btn.click_button()
